from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import MyUser

class ProfileInline(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'MyUser'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class ProfilDetayi(admin.ModelAdmin):
    model = MyUser
    can_delete = False

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return  False

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(MyUser, ProfilDetayi)