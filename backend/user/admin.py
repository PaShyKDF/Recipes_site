from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Subscription, User


class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name",
                    "is_staff")
    list_filter = ['email', 'username']


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'subscriber'
    )


admin.site.register(User, UserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
