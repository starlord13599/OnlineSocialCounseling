from django.contrib import admin
from django.contrib.auth.models import User, Group
# Register your models here.

admin.site.unregister(Group)