from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        # None is the title of this section
        # and it appears on the top of the page.
        (None, {"fields": ('email', 'password')}),  # First section
        (_('Personal Info'), {'fields': ('name',)}),  # Second section
        (_('Permission'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        # Third section
        (_('Important dates'), {'fields': ('last_login',)})  # Fourth section
    )
    # If you wanna add extra fields simply add ('new_field') at the
    # dict at the 'fields' voice.
    add_fieldsets = (
        (None,
            {'classes': ('wide',),
             'fields': ('email', 'password1', 'password2'),
             }),
    )


admin.site.register(models.User, UserAdmin)  # register(models, referred_admin)
admin.site.register(models.Tag)  # here we use the default admin
admin.site.register(models.Ingredient)
