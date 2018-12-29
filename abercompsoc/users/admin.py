from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from abercompsoc.users.forms import UserChangeForm, UserCreationForm
from abercompsoc.users.models import Role

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("roles",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "get_full_name", "is_superuser"]
    search_fields = ["name"]


admin.site.register(Role)
