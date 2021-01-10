from django.contrib import admin
from .models import *
from .models import User, Address, Toy, Tag
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserAdminForm


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "email", "phone")
    actions_on_bottom = True
    empty_value_display = "-"
    form = UserAdminForm
    search_fields = ("first_name", "last_name")
    readonly_fields = ("password_change_link",)
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def password_change_link(self, obj):
        return format_html(f'<a href="/admin/toys/user/{obj.pk}/password/">Change Password</a>')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "zip_code", "country")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    date_hierarchy = "created_at"
    autocomplete_fields = ["tags"]
    search_fields = ("name", "description")
    list_filter = ("type",)
