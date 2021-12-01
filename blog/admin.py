from django.contrib import admin
from .models import User_modified, User_origin, Singer_origin

admin.site.register(User_origin)
admin.site.register(User_modified)
admin.site.register(Singer_origin)