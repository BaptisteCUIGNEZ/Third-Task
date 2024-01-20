from django.contrib import admin

# myapp/admin.py
from django.contrib import admin
from .models import MyFileModel

admin.site.register(MyFileModel)
