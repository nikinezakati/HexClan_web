from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import user


class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', )
admin.site.register(user, userAdmin)
