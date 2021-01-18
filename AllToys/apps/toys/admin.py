from django.contrib import admin, messages
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserAdminForm
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from .services.send_weekly_report import send_weekly_toys_count, send_weekly_email_report,total_salary_expense_for_this_month
from django.utils.translation import gettext_lazy as _



class UserToysInline(admin.StackedInline):
    model = Toy
    extra = 0
    fields = ("name", "description", "type")
    # fields = ("name",)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "email", "phone","password_change_link")
    actions_on_bottom = True
    empty_value_display = "-"
    form = UserAdminForm
    # search_fields = ("first_name", "last_name")
    readonly_fields = ("password_change_link",)
    fieldsets = (
        (None, {'fields': ('username', 'password',"password_change_link",)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'age', 'address')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    inlines = [UserToysInline]
    actions = [send_weekly_email_report]

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


class CompanyEmployeesModelInline(admin.TabularInline):
    model = Company.employees.through
    extra = 0
    # fields = ("first_name",)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("company_name", )
    autocomplete_fields = ["employees"]
    search_fields = ("first_name",)
    inlines = [CompanyEmployeesModelInline]
    actions = [total_salary_expense_for_this_month]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ("first_name", "last_name", "password_change_link")
    search_fields = ("first_name",)

    def password_change_link(self, obj):
        return format_html(f'<a href="/admin/toys/user/{obj.pk}/password/">Change Password</a>')

