from toys.models import *
from django.core.mail import send_mail
from django.contrib import admin, messages
from django.http import HttpResponseRedirect


def send_weekly_toys_count(user):
    toys_count = Toy.objects.filter(user=user, user__is_active=True).count()

    send_mail(
        'Your toys update from AllToys!',
        f'You have {toys_count} active toys at the end of this week!',
        'info@alltoys.uz',
        [user.email],
        fail_silently=False,
    )


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


def send_month_employees_salary(company):
    employees_of_company = Employee.objects.filter(company__company_name=company)
    employees_salary = employees_of_company.value_list("salary", flat=True)
    sum_employees_salary = 0
    for employee in employees_of_company:
        employees_salary += employee

    send_mail(
        'Your toys update from AllToys!',
        f'Your Company {sum_employees_salary} $ spent for salaries in this month!',
        'info@alltoys.uz',
        [company.company_email],
        fail_silently=False,
    )


def total_salary_expense_for_this_month(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, "Multiple Company selected, please choose one and only one.",
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())

    company = queryset.first()
    if not company.company_email:
        modeladmin.message_user(request, "Selected Company does not have email address",
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())

    send_month_employees_salary(company)

    modeladmin.message_user(request, "Weekly report sent to user email: %s" % company_email, messages.INFO)
    return HttpResponseRedirect(request.get_full_path())

