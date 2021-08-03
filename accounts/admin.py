from django.contrib import admin

from accounts import models

from .models import User


admin.site.register(User)