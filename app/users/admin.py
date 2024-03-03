from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("유저 정보", {"fields":("email", "nickname", "is_business", "password")}),
        ("Permissions", {"fields":("is_active", "is_staff", "is_superuser")})
    )

    # 유저를 만들 때 보이는 화면
    add_fieldsets = (
        (None, {
            'classes' : ('wide', ),
            'fields': ('email', 'nickname', 'is_business', 'password1', 'password2')
        }),
    )

    # 표에서 보이는 정보
    list_display = ('email', 'nickname', 'is_business', 'is_active', 'is_staff')
    search_fields = ('email', 'nickname')
    ordering = ('email', )