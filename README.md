# Проект «Foodgram»
## «Фудграм» — сайт, на котором пользователи публикуют рецепты, добавляют чужие рецепты в избранное и подписываются на публикации других авторов.Пользователям сайта доступен сервис «Список покупок». Он позволит создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

### Стек технологий:
<img src="https://img.shields.io/badge/Python-3776ab?style=for-the-badge&logo=python&logoColor=yellow"/>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Rest framework-092E20?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAfQAAAH0CAMAAAD8CC%2B4AAAABGdBTUEAALGPC%2FxhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAkFBMVEX%2F%2F%2F8dMSQdMSQdMSQdMSQdMSQdMSQdMSQdMSQdMSQdMSQdMSQdMSQdMSQdMSQdMSQdMSRjcWiNl5BVZFqpsaz8%2Ffzh5OJxfnXFy8fv8e9HV03T19Q5Sz8rPjK3vrl%2Fi4ObpJ5YZ16FkInBx8Lt7%2B6jq6be4t92g3o7TEEsPzKyubTP1NGUnpdndWxKWk%2F%2F%2F%2F%2FQyt1tAAAAEHRSTlMAIEBggMDgMHCg0FDwsBCQOThaYQAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfhBxYUNjKMen2NAAAW5klEQVR42u2da3fqOg6GuSSQhEtTIC0UKOXWlp6y%2F%2F%2FPO0Ap5ZbEcmxHsvV%2BmFlrpqTFz5YsybJSqbBYFqpaq9U9z%2FN3asR31dj%2Ff7sfqddqVV4vymrWAi%2F0oxisyA%2B9oNbkFaSkWmsHux0XVnsHv1Xj9cRu3HUvzYPLq%2BF7dTZ7nOYdhFGsUVEYsNGjsm%2B9vM%2FJs81jMHBPxe4N2%2Bk9NvlSgcclicGXoWbQiUtWJ2BXb07dVtgom%2FgxsA9bXeahX9XAxwH85OkDLuJpVfMhwkX8GNQ%2FsKPXRhyJU7%2Fr6Jm7Y8SZuwZVA5Re%2FY6f5%2F1djbr10pMziDp1jucLu%2FWwTQn5Xu2Q3XwRI6fi1m%2FdPJu7M0bO5l5MdaJGfmbudaYI8useYSM%2FM3ePvbyoqqENxH8Ucg4nohqy2npR%2BXwIm6e6ZcgP2Hlzz0SOvtYqpwZjdw05Y3cSOWN3Ejljv1HLAeQH7C1mfZRtSVqWOIE7qOoQ8gN2Ltd0Laq%2BiSp0vDhrR40dqrbnMHJX4rdbORvRubaZ89Ze6XouI9%2FLvXNXdz27sz6%2BSqrBVZ86Dvn4wMmY%2FZ7agSPIm04HcNfynWigdD6Au5b9SXuTfJOrekWWGzubuXPGzmbunrFz0J4uS8P4LgftmfItLNC12MzzjN26At0DQ83Xg1XIOYITk03xXJ1du6iLt6Vh1sWOKHnZ0UtVZdcOc%2FEWnLxx1A528eSjeK67Soh2VbbLzRJS6hDe2DlTkxXd3I23c3lR3dgDRldEJE9gODsvqJBeCMdnaoVF7dyNKzIqRKtO0%2BQQTonahIJ4DtuVUScTxNcZljoROXbjVE2pSKRunKopFoHUjZm7R52ZO0e9y%2Bm5FkWIyzTM3D3qzNw96szcPerM3D3qzNw96szcPerM3D3qzNxB6szcFHU8zLn2akxoKrLM3D3qzNw96hR6Jh5713rs9%2Fu3%2F2vvkcCXQdBVQaE3apAIq5f6kP6T6DOenvV%2BndI7qFoUPKI48%2BQp9SFD8YeMNH%2BfkrslafQ6A6AnSh7yovf7lNsZXaXR62wcel%2FzF2qXeAuCSiHONksvtTRH5b6acej6v5LPCbp70MtK1%2BlcalDCa4wLejnpOolkTSH0ITLoZSRulC6m2gndfOJG6gTdTujmQ3hSs8IshR53zDKnNRPQVuhmpwwSCuKshm4ymCNSfXUAurl6LLk2SHuhmwvmyLXKWAzdVGWO3kgZm6GbaakgOC7MauhGajQEe9ythm6iF57iu7bshq7%2FzV7EMnQnoOvO1rskZ0HaDr2tN2%2BjOdvZduh6%2B2iIDoO0HrrOjgqqw53th64xb6N6I9l%2B6PryNrLvWHMAuq5T1iZV5k5Aj5vs3N2DHrFzdw%2B6DgdP17m7Al2Dg6f8yi1HoCsv0ZB%2BR4cj0FWXaKh1xbkJXXHHHO1XYrsCXW0jPMkDVQehqzxk7TYYOg3oDXWHrIRTdHXQEwrQ1SXrVeLMXYIeq4rlyL8V2zj0SXnfVVGyTjyKiy2cLpUlNbEc8SgutnG6VIYaHMWpg45t5kyqFMRyNPtfNUB%2FHok%2BYvRc6rdV0Btrw2BvIoG3KhW%2B00g%2BXXMQeuG0jXy65iL0gmlbzYY1cA56XGNDdw96IVOnX5dxE3qhCg39uoyj0AtUaOgNGmHoR9VdN3QXoTdcN3QXoUubui2G7iT0huOG7iR0SVO3xtDdhN5w29DdhC5l6vYYuqPQG04buqPQJUzdjqq709DBFXg7jtfchg4%2BbKNo6JP%2BSVOGDjd1Sg0zk36vNxzedLA9DV97zz%2F0XYUObKEh0hnXnw3yrpiNhr1HZ6GDuuW6BL7QYw9ypVAF9JeU3ePX4fwK0SJBGmOx97pPZlqAZ0J%2FeRJ%2BRg%2FNQkF64FH3uk9m40SfUn%2FtK8U9om1FYWb6rJN4Fq8R4CEvaNZLvECDdkzgZDBKkpKgQx6CZ1sXHimIdWRcf5jol2XQhYfL4czXjCC3D7pg1obyyuKLGeT2QRe8zohwTuB0kCQMXU4B0TDueZQwdFlFJMO4yTBJGLq8mgTDuMdRwtCLKCQXxhnczW2FLhDK4arGTcYJQy%2Bq%2FKocqtG%2FL6OEoRdW7phgVN0Tz%2BaZ2wg9t5cCU5L%2BnCQMXYUCOkl6KcythB6RSdLLYW4l9JxU%2FcF15nZCf6Bxl%2BkxwQZ9RBh6g4R3LyFXy4M%2BJAw9079j8e7T0phbCv2BgHcfJgzdlH%2FH4t3fEoZuzL8j8e79hKGb8%2B84KjMlbuj2Qo%2BQ191fE4auXlXUdfdSnbu90APMd9KnTwxdh3zMV1V7CUPXovv9MyjmfE9GDF2PWng7IgcJQ9ejEG05blKM2Pi113s8jgaY9d6GTwz9pAbaclwBQx%2F37i11f%2FbK0H%2FURJqwSRv60yz9nbbTMUPfK0DaBitp6MPsRX5h6Hvda4ola%2Bjj3CVm6AfdMscwIlImRx%2FN8p%2FL0A%2BqoRwoJZGjj0XGuzD0gzyMNViJXsjBVOTBDP0gH%2BOWDj9eG4g9mKH%2FCOGWPtHFnKEfVcO3pc90MWfoR3n4tnToreSh8JMZ%2Bo%2BuN%2FXyRxFAvftoKvxohv6jNrrCO9S7AxaWoR%2FVxDZ%2FAtjrPgA8mqEfVUd2lj7V5twZ%2BkkhsuZn4I1F0Eh1hn5UhKw086bP0Bn6SchKM2N9hs7QT6qhaqAAbukThi6lAFUcB7vi8Ap7OEP%2FVYgqjoMdpT8zdDlFqOI42AnbFPZwhn4SqnocKI4bAh%2FO0E9qYqrHaYzdGfqZ6ojOVUENq%2BA1ZegneYjOVWHBu043Yjl0H9GFJlDwPmbo0mogCt5B0AfQpzP0PyEqwoLOVcHvr2Xof6rhuZgOgv7I0OXVwtMUCYIOXlKG%2FicPzzQCUPA%2B1fl026GHeDphtWZsDP1MPppOWIZuTG08N5oYujHhmTvC0I2pieZmOkM3phqaYTMM3ZgCNOMIGLoxeWiGBjJ0YwrRzAFm6MbkoxntD4LOZdgiirCk6bARQwy9kNBA56NVs9BRvMQDBP2NoRdRFUltBtb2Du2AZugXqmGBDmqXGjH0otARNL1DZ49MgE9n6OeqIynIAVuggVfZGPqFPCzQYZcdoO2wDB0ldFh15omhF4SO4m1swEEUL7CHM%2FRz%2BWigw64qvzF0G6DDhhIAkzaGjhM6cKIYLH5n6NfQMbyODTwZFhbKMfRzNZCct%2Bz0pNHUGfqF8EB%2F1WjqxqFPkSwqdujQIdCQ81Xj0FEzRwT9BQgdkqszdKTQwe%2FnGhse8j9i6OoFfleT%2BNhIJdAThq5e8LeymX1xD0PXIIkXrRp9RRdD16GxBHWxfZ2ho4U%2Bg0NPxkJNNAwdLXSpF2mLvFSZoV%2Bqiwg69H1NRw3za54MHa2ly7xVWQw7Q8cLXeb96cetfZa1t08YOmLovURe416avU9fGTpi6JOkmMavvVm%2F3z9Y%2Fe6%2F%2B8%2B93tsQGCkwdNMaJKUr7U%2FrM3Skps7QCUIHvoeRoVsBfTpi6M5Bl6rFMnTi0GWOXRg6GDqOFuiTXpBCn1kDPUJz2eFPPZzQe9ZAx3PDBY2DZ%2BilaDJi6M5Bh95rY%2Bhw6DiGEsgvsCHoQ2ug45lEcakBQ3cPeonU3YCOYqTYjcaUoY9RLumv6liGB95o%2BooMOuQZQ5RL%2Bis0EyPxeHg3oKMYCIyHuv3Qq1hGf9%2FVMyLoE3ugo5n3fl8vIzTQ%2B5ZBx%2FA6jxRNhyShD%2FCu6O%2FrPPDVYc80G%2BGADtpqephX1Efziq50TYYooPesgR6ieRlflp5HCKAPrIHuoXntZqamvfKhg%2FzNI%2BbVDNC8YDfPxw%2FKhq73HWImVUPzKm082FN%2Bf2IN9J9XaVcoQN9h75nY21MmUcJeN4J6YOQP80qbBvVdSKf%2F7C0lBoO142New%2FYROupE%2Fcrc3560Mn9LMVLQ5jLCvIL%2BETruRP1aL3q4j4Zvs36qXwa5GNRV2PAIHXuifmvvs1eF%2B%2FvTsJeB%2B6Ap6IGvmNfOO0JvUYN%2BMPjZ61Nh2m%2B9vtBcYVh%2FLuraTOsInUCinmKA%2Fd5gCLf58XDQe%2B5DXuMIu0E9w7xmtSP0ClXoR%2FUfe73X4TjPrIevvR1rqRwa5lPwvz29gu8Oo7xe9pNmdv8ETtqPoOn3JwUfCxyQMUG8Qo0TdEI5WykCXprH%2FFX8E3Ry4bthwWpCqDM27wQdZ%2Bs7GgG9O%2Bq%2BmfoJOokjl%2FIEPNlFHbw3T9ArDDZLwHoAjeAddW9k%2BYLenMb8XaIz6LSq74YFbNJDfZEtPIOOvmOqREGnWL5h%2FjLBGXSyhVgDgrbsPGP%2BMrUz6BVmq8rQUdfjzuM4juTUGfoT5i8TXUDnSC5F%2FcSmLT28gM41uRSB79eg7nmvX0Dnmtx9wecTo%2F46zQvodDpijQo%2BiRx1q1T7kjmfrt4V%2FPIk6oTNv4LOp6t3JDF8HvU9B%2B8KOpdnbiUxhRy1d78szXB55p6mEt22qL17fM2cN%2FUbSUxDQH235WZL5039RjLXZN9QfyPvBjpv6peSelkY6rr77ZbOm%2FqlpGbY4Q7jbrf0SqXDpAsyx90oFXfuQOdGij%2FJjb3APTPwooGCy%2B%2BKmCM39OvCu2WXmwpqKjnvArmhN%2B4x5zP1H73I3oBGbujhXegkr6krl%2FTLXlFfbIn%2FLqZfqsvEC7xQYoQ7R4%2Fj7l3oXIktMpEU9WWm%2BF4NlpO2vYrMHsb9rp74fsJWwfxiDyMqNoH2BfvXq6ZAd7kRelpsHiV2537V%2FHyuB2eRz4pNqkKeou%2F0kArd0aLctOjU2SfUTVIHNVOhu1mUK%2F7GEPQbeko5zln%2F%2Flx86CjuHqmDHjKgO%2Bff%2BwrmzL4R%2BJ4Z3t09%2Fz4tPkQee%2Fl1ryzvzv7dTuaZ3t3R%2BL0IdhLMs727q%2FWZx6HVzKNs5s7W3%2FtDe5mn1t25%2Ft4f2Mo8ve7O56vg14ChL7gf1clj7vZMCgj2EeqZE%2Beq50Lvuj2eQDhxH%2BOvvR7V7uZCd74%2FUgz7K%2F4zll%2BF%2Bcy5%2Fz2e5ibuIyrb%2BV5NAejc%2Fx7n1WvG2JsgzxWJMOf7TT%2FYUxP3EepXcN0oEILueCh3Ukq9ZkjJzMXCOA7lsrE%2FkUnUjgrFmHMo96erxH3UoxO0H9UUhM7jgVOwD2h59r0iUeY8KfYS%2B9uIKnKRatxJHMpdaNobDkkivxkMmiUeNWWJPAB0vsBqiboA6Jy12aEQwtzxu4zWqAqCznfVbZAPY84DJG1QDQidTd09Q%2BcCjQWqg6HzsTp1NeDM2dQdNHQ2dQcNnU3dRUNnU3fQ0NnUXTR0NnUHDZ1N3UVDZ1N30NB5GjhZtQpA5wo8TflFmPNhG03VCkFnU3fP0LmFhqSqBaFztxw9hUWZ83VGcmp3C0PnHnhq8ioKxBUaUmqoYM4VGlpqKYHOaRsl%2BWqYc9pGSVVF0DmWoyNPFfNK16FYbr5YLJfLVZLs%2FnO9WMxp%2FfWNrjLoJcRyecP73pfrj0%2BZD%2F5pefPZzeLr9sf%2B%2B95uJH%2FDQUaXrVVRqA426D88FhuF0OdfqT%2F6taUBvaOSeaXaxgg9SVY32GWhfy5FfxFe6O2qUujGJwoKr%2BlqqwT6QvzfF17oQUWxfKTQk%2BS7OPTNl8gH3re4ofuqmZseLgdZ1nVR6Jv%2FBD%2FytcEMvakcuuFkPZGlLgP9P%2BHPrOZ4oXsVDYrQQk%2B2haCvxT%2Bz%2BocWeqSDuVkHD1vY1WcB6FvAL%2FrA696bWqAbdfDAlV0XgP4O%2FDU4oXsVTYrQQk8%2BpaEvxD%2FxX4wWeqSLeaXZRgt9LQ1d3NCPmwhG6O2mNugGSzRQ6CtZ6P%2FEPzCP0UIPKhrlY4X%2BSwQM%2Fda7vy%2B28%2Fl2sdgftZ1rEaOF7utkbq43Fgx9IQn9puT%2B9fdHfJ6fun3FaKG3u1qhGztkzVy7f%2Bvbtf0S%2BeAdvae5jB9tPo4%2F8L6R%2BUvNqFXRrAcE0O%2FtxEtJBukh4a%2Fme2ewr8pghf6gm3mlayZvy1vK77QfKAw9WX5cG%2FV2dajKIIUedbVDN5S35S3lXB%2F0fUK%2BvuyT2izk%2F1Ld0pmt%2FcnIUBJj0NPT9GvySKHXK0Zk4k5j3lKuhaHnhNXLnBD%2Fe4sbemiGuZFtPWcpP8QDuRzo37k%2Ft1pv8UI3saH%2FyEDHXOZSbiEpWw50oTO29%2B9PnNBVd8WVm60bKM78%2FPxmJfbT3yjz9FbFoDx00OeS0IVbKFZbfNC9ilF1kEGXOHA5fuBT%2BANrbNA7ZplrD%2Bag0NfS0AEH6mtc0M0FcYZqNFDon%2FLQAX2Ra0zQzVRlTAZzsoYuA30jTn2BCHqrUoICPNBXmyLQAdRXn2igB5VSFKKBLtUCffbbxG643HfwJUEPKyXJRwJ9EReEHsdbwVa51QYHdL8s5jpDeAjz77g49Dj%2BEMO%2BRQHdfOD%2BJ331WADzj1gJ9Dier2X8exnQTVZfDSZuwuj%2B%2Bxergr738us8e18igF5GsmYicZPOoeQYzP%2FcxWZ70wd7sakjgN6qlKx6udDnShhs3q%2F%2B9Wzmi%2B%2BlmIMwD71eNnNd6boodDXedr%2BZf90eo82%2FVwihB%2BUz15SupyzlV66pyzD4OVN%2Fv9McdSeBLxt6iIG5HuopSznPNXUJBqcj9a%2FbetvNL3wvGToS5lqopy3le56pSzA4s%2Bb1dXv7Aln0joa5jiJN2lJ%2B5Jm6eMp2fyjB%2B%2BJfFvOrsUamoUdomOugnraUd7qb5sWgf948cbX83t9hnC%2FWq7xSkGHoZRbiDFBPXcrvHFMHQ18mIJVZe8fFXD311KX8zMnVodAXMObLuDzo2Jgrp56%2BlF%2FZIID8Plcw6B%2FlQcfHXDX19KWcZ5s6EDrQub%2FHpUHHyFwx9YylfM80dRh0oHNPtqVBx8lcLfWMpfzINHUY9A%2BYd%2F%2BOy4KOlblS6hlLeSdrW0q793%2BAKXLJf5uyoONlrpJ61lKus9wuNBAXb4%2B7z9wIdMzMK%2BoqsllL%2BZkVYMGzL9H2uOUmLgl6iJu5MuqZS7nMSKUkUu7NQmRnX8j8pWqYI0eujHrmUm4zTF0C%2Bh57bpfUZ1wWdALMFXVVZC%2Fle7qpS0Hf%2F0PK2tvX%2F2T%2F0uJC0TORr7p26It0U5eFvuf%2Bfe%2Bmy%2BrrYyP%2FlxYWgt4oMbXovnP933bxvVwegobD2%2Fi2%2F0r9c9ql90CKq0mXOiqV3esMUzViYsUVVSkxr1S6%2FP7twvKxp%2Be3CplaMZFI1a4VMLciIpKqXYtwEF%2B6KIXtl2pyOCepiFTYfhXOdZifjDr0QrhzeUwQLo80ct7YJUR3O%2F8T12lgolaRSdnYOWMHCH3DhKjq7OJFXTuZQ7V8ce4m6NoJZ2p3XPwDE83Xgy2u%2FVccxee6dgui9htj53O3TBE8UxNRwMaebuZEz1fyxfFcmuyK4K7EVdm7Il93ZWNnM2djd9zMj8bOYfyZfPvN%2FEccxv%2FK3qD9VlVurjioY8WJmrBaDUbesLAEl62u8wGdZ2cJLsfHOx3Q%2BW55dvbxLnr2M3lOxvFtJ1LzjK3dwV4qazqieGvnzRykmkPY%2FRrzPsqViM7p%2BO1WdQewNyxqdWXsjJyxM3LGzshzsVsYyfuMPE%2B2JXCcpAmpalGVLuRSjKi6dtTk206enhZQnXzbbMRbOVzNkLC5t0NXGh6Ve%2FmAqLlHAft1t8ydjVyBuddJtc526mzkSlSl4uajgDM0lW7%2BAX2FtvHAbt0t7kxcI3eUfj5i4npVDZDV5n3ex02o2wqROPpG2OJY3ZyaQemJXCdgp25eNa80T%2B97fGBaKnjDJbs2A8egZj00FNRHYZ1dOiaTD%2FSSj8KADRypzXu%2B8sC%2B4Xts3%2FiNvuWFKnb6th96LTZvWmZfC3bwJXx%2BtIMd1Ni4Sataq9U9z%2FN3aqRh3mn3I%2FVajctrLCv1P2iykwAlSR0dAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE3LTA3LTIyVDIwOjU0OjUwKzAwOjAw1zCZkQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxNy0wNy0yMlQyMDo1NDo1MCswMDowMKZtIS0AAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AAAAAElFTkSuQmCC&logoColor=white"/>
<img src="https://img.shields.io/badge/PostgreSQL-50b0f0?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/CI&CD-B8860B?style=for-the-badge"/>
<img src="https://img.shields.io/badge/github actions-4B0082?style=for-the-badge&logo=githubactions&logoColor=2088FF"/>
<img src="https://img.shields.io/badge/docker-1d63ed?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/nginx-006400?style=for-the-badge&logo=nginx&logoColor=32CD32"/>
<img src="https://img.shields.io/badge/gunicorn-6B8E23?style=for-the-badge&logo=gunicorn&logoColor=1d692d"/>
<img src="https://img.shields.io/badge/JWT-2980b9?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAACVBMVEVGUViMoa/i5+sa4fYGAAAALElEQVQ4y2NgoAtghAMghwkZUFMBgoKJ0l/BqDdpoYCgG+iggA7eJEMBjQEA95EC+R9NCHIAAAAASUVORK5CYII="/>
<img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=FF4500"/>
<img src="https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white"/>
<img src="https://img.shields.io/badge/yaml-FF0000?style=for-the-badge&logo=yaml&logoColor=white"/>


### Порядок установки API:

Клонировать репозиторий и перейти в него в командной строке:
```sh
git clone git@github.com:PaShyKDF/foodgram-project-react.git
```

```sh
cd api_final_yatube 
```

**Cоздать и активировать виртуальное окружение:**

```sh
python3 -m venv env
```

```sh
source env/bin/activate
```

**Установить зависимости из файла requirements.txt:**

```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

**Выполнить миграции:**

```sh
python3 manage.py migrate
```

**Запустить проект:**

```sh
python3 manage.py runserver
```

### Запуск на сайта:

**Создать файл .env в корне проекта и записать данные для подлючения к базе данных и настроек settings.py**
```.env
POSTGRES_USER=django_user
POSTGRES_PASSWORD=password
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
DJANGO_KEY='django_key'
DEBUG_VALUE='True'
ALLOWED_HOSTS='site1,site2,site3'
```
**Запустить сборку проета**
```bash
sudo docker compose -f docker-compose.production.yml up
```

### Примеры запросов к API:

**Создание пользователя**

POST ```https://yapract-foodgram.hopto.org/api/users/```

Данные запроса:
```json
{
    "email": "vpupkin@yandex.ru",
    "username": "vasya.pupkin",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "password": "Qwerty123"
}
```
Ответ:
```json
{
    "email": "vpupkin@yandex.ru",
    "id": 0,
    "username": "vasya.pupkin",
    "first_name": "Вася",
    "last_name": "Пупкин"
}
```
**Получение токена**

POST ```https://yapract-foodgram.hopto.org/api/auth/tocken/login/```

Данные запроса:
```json
{
    "password": "string",
    "email": "string"
}
```
Ответ:
```json
{
    "auth_token": "string"
}
```
**Получение рецептов**

GET ```https://yapract-foodgram.hopto.org/api/recipes/```

Ответ:
```json
{
  "count": 123,
  "next": "http://foodgram.example.org/api/recipes/?page=4",
  "previous": "http://foodgram.example.org/api/recipes/?page=2",
  "results": [
    {
      "id": 0,
      "tags": [
        {
          "id": 0,
          "name": "Завтрак",
          "color": "#E26C2D",
          "slug": "breakfast"
        }
      ],
      "author": {
        "email": "user@example.com",
        "id": 0,
        "username": "string",
        "first_name": "Вася",
        "last_name": "Пупкин",
        "is_subscribed": false
      },
      "ingredients": [
        {
          "id": 0,
          "name": "Картофель отварной",
          "measurement_unit": "г",
          "amount": 1
        }
      ],
      "is_favorited": true,
      "is_in_shopping_cart": true,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "text": "string",
      "cooking_time": 1
    }
  ]
}
```
**Создание рецепра**

POST ```https://yapract-foodgram.hopto.org/api/recipes/```

Данные запроса:
```json
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
```
Ответ:
```json
{
  "id": 0,
  "tags": [
    {
      "id": 0,
      "name": "Завтрак",
      "color": "#E26C2D",
      "slug": "breakfast"
    }
  ],
  "author": {
    "email": "user@example.com",
    "id": 0,
    "username": "string",
    "first_name": "Вася",
    "last_name": "Пупкин",
    "is_subscribed": false
  },
  "ingredients": [
    {
      "id": 0,
      "name": "Картофель отварной",
      "measurement_unit": "г",
      "amount": 1
    }
  ],
  "is_favorited": true,
  "is_in_shopping_cart": true,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "text": "string",
  "cooking_time": 1
}
```
**Добавить рецепт в список покупок**

POST/DELETE ```https://yapract-foodgram.hopto.org/api/recipes/{id}/shopping_cart/```

Ответ:
```json
{
    "id": 0,
    "name": "string",
    "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
    "cooking_time": 1
}
```
**Скачать список покупок**

GET ```https://yapract-foodgram.hopto.org/api/recipes/download_shopping_cart/```

**Добавить рецепт в избранное**

POST/DELETE ```https://yapract-foodgram.hopto.org/api/recipes/{id}/favorite/```

Ответ:
```json
{
    "id": 0,
    "name": "string",
    "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
    "cooking_time": 1
}
```
**Мои подписки**

GET ```https://yapract-foodgram.hopto.org/api/users/subsciptions```

Ответ:
```json
{
  "count": 123,
  "next": "http://foodgram.example.org/api/users/subscriptions/?page=4",
  "previous": "http://foodgram.example.org/api/users/subscriptions/?page=2",
  "results": [
    {
      "email": "user@example.com",
      "id": 0,
      "username": "string",
      "first_name": "Вася",
      "last_name": "Пупкин",
      "is_subscribed": true,
      "recipes": [
        {
          "id": 0,
          "name": "string",
          "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
          "cooking_time": 1
        }
      ],
      "recipes_count": 0
    }
  ]
}
```
**Подписаться на пользователя**

POST/DELETE ```https://yapract-foodgram.hopto.org/api/recipes/{id}/subscribe/```

Ответ:
```json 
{
  "email": "user@example.com",
  "id": 0,
  "username": "string",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "is_subscribed": true,
  "recipes": [
    {
      "id": 0,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "cooking_time": 1
    }
  ],
  "recipes_count": 0
}
```
**Список ингредиентов**

GET ```https://yapract-foodgram.hopto.org/api/ingredients/```

Ответ:
```json
[
  {
    "id": 0,
    "name": "Капуста",
    "measurement_unit": "кг"
  }
]
```

Ссылка на сайт: ```https://yapract-foodgram.hopto.org/```  
Почта адина: ```admin@ad.ru```  
Пароль от админки: ```12341234```