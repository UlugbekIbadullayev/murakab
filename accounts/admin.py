from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

User = get_user_model()

class UserAdmin(DjangoUserAdmin):
    ordering = ('pk',)
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
    )

admin.site.register(User, UserAdmin)




