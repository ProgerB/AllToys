from django.contrib import admin
from .models import *

admin.site.register(Markets)



"""7-dars 4-topshiriq """

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name","phone")
    search_fields = ("first_name", "last_name")

class CompanyEmployeesModelInline(admin.TabularInline):
    model = Company.employees.through
    extra = 0
    # fields = ("first_name",)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", )
    autocomplete_fields = ["employees"]
    search_fields = ("first_name",)
    inlines = [CompanyEmployeesModelInline]
