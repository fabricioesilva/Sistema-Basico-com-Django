from django.contrib import admin
from .models import CustomUser, UserEmailCheck, Preferences, DeletedUser


class UserEmailCheckAdmin(admin.ModelAdmin):
    fields = ['user',  'uri_key', 'user_email', 'date']


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserEmailCheck)
admin.site.register(Preferences)
admin.site.register(DeletedUser)
