from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,UserProfile

class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_active', 'role']
    # list_filter = ['is_staff', 'is_active']
    # search_fields = ['email', 'username']
    ordering = ['email']
    filter_horizontal = ()
    fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'role')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superadmin', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('date_joined', 'last_joined', 'created_date', 'modified_date')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'role', 'is_staff', 'is_superadmin'),
    #     }),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
