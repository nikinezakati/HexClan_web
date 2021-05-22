from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import user
from User.models import artist_rating

admin.site.register(user, UserAdmin)
admin.site.register(artist_rating)


