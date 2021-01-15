from django.contrib import admin, messages
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserAdminForm
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from .services.send_weekly_report import send_weekly_toys_count


class UserToysInline(admin.StackedInline):
    model = Toy
    extra = 0
    fields = ("name", "description", "type")
    # fields = ("name",)


def send_weekly_email_report(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, "Multiple user selected, please choose one and only one.",
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())

    user = queryset.first()
    if not user.email:
        modeladmin.message_user(request, "Selected user does not have email address",
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())

    send_weekly_toys_count(user)

    modeladmin.message_user(request, "Weekly report sent to user email: %s" % user.email, messages.INFO)
    return HttpResponseRedirect(request.get_full_path())


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
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'age', 'address')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    inlines = [UserToysInline]
    actions = [send_weekly_toys_count]

    def password_change_link(self, obj):
        return format_html(f'<a href="/admin/toys/user/{obj.pk}/password/">Change Password</a>')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "zip_code", "country")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


class ToyTagsModelInline(admin.TabularInline):
    model = Toy.tags.through
    extra = 0


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    date_hierarchy = "created_at"
    autocomplete_fields = ["tags"]
    search_fields = ("name", "description")
    list_filter = ("type",)
    inlines = [ToyTagsModelInline]



