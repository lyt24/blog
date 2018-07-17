from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


# 创建行内链接，指向的模型是Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


# 继承了括号里的，在里边加上ProfileInline
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'nickname', 'email', 'is_staff', 'is_active', 'is_superuser')

    def nickname(self, obj):
        return obj.profile.nickname
    nickname.short_description = '昵称'

# 取出user,重新注册
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname')
