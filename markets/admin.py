from django.contrib import admin, messages
from .models import *
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


admin.site.register(Markets)


"7-dars 5-topshriq"

#
# def send_weekly_email_report(modeladmin, request, queryset):
#     if queryset.count() != 1:
#         modeladmin.message_user(request, "Multiple user selected, please choose one and only one.",
#                                 messages.ERROR)
#         return HttpResponseRedirect(request.get_full_path())
#
#     user = queryset.first()
#     if not user.email:
#         modeladmin.message_user(request, "Selected user does not have email address",
#                                 messages.ERROR)
#         return HttpResponseRedirect(request.get_full_path())
#
#     send_weekly_toys_count(user)
#
#     modeladmin.message_user(request, "Weekly report sent to user email: %s" % user.email, messages.INFO)
#     return HttpResponseRedirect(request.get_full_path())
#



"""7-dars 4-topshiriq """

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ("first_name", "last_name","phone", )
#     search_fields = ("first_name", "last_name")
#
#     fieldsets = (
#         (None, {'fields': ('username', 'password',)}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'age',)}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser'),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )


    # def password_change_link(self, obj):
    #     return format_html(f'<a href="/admin/markets/employee/{obj.pk}/email/">Change Password</a>')

# class CompanyEmployeesModelInline(admin.TabularInline):
#     model = Company.employees.through
#     extra = 0
#     # fields = ("first_name",)
#
#
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ("name", )
#     autocomplete_fields = ["employees"]
#     search_fields = ("first_name",)
#     inlines = [CompanyEmployeesModelInline]
