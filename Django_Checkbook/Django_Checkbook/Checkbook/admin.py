from django.contrib import admin

# Register your models here.

# add model to admin

from .models import Account
admin.site.register(Account)