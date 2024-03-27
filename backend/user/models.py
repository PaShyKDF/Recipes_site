from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    username_regex = RegexValidator(
        regex=r'^[\w.@+-]+\Z',
        message='Некорректное имя пользоватея'
    )
    username = models.CharField(
        validators=(username_regex,),
        verbose_name='Логин пользователя',
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )
    first_name = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        blank=False
    )
    last_name = models.CharField(
        verbose_name='Фамилия пользователя',
        max_length=150,
        blank=False
    )
    email = models.EmailField(
        verbose_name='Email пользователя',
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    password = models.CharField(
        max_length=150,
        verbose_name='Пароль'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
        constraints = (
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            ),
        )

    def __str__(self):
        return self.username


class Subscription(models.Model):
    user = models.ForeignKey(User,
                             related_name='user',
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    subscriber = models.ForeignKey(User,
                                   related_name='subscriber',
                                   verbose_name='Подписан на',
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'подписку'
        verbose_name_plural = 'Подписки'
        ordering = ('user',)
        constraints = (
            models.UniqueConstraint(
                fields=['user', 'subscriber'],
                name='unique_user_subscriber'
            ),
        )

    def __str__(self):
        return f'{self.user} подписан на: {self.subscriber}'
