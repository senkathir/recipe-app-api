from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
#This is the general convention to convert any python string to human readable
#text. It gets passed through translation engine(converts to other language)
from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email','name']
    fieldsets = (
    #each bracket is a section
        (None, {'fields':('email', 'password')}),#Title
        (_('Personal Info'),{'fields':('name',)}),#comma used at end of params
        #having one field otherwise it will be considered as string
        (
            _('Permissions'),
            {'fields':('is_active','is_staff','is_superuser')}
        ),
        (_('Important dates'),{'fields':('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email','password1','password2')
        }),
    )

admin.site.register(models.User, UserAdmin)
