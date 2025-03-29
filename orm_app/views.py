from django.db.models import Count
from django.shortcuts import render
from .models import Countries, Locations, Jobs, Employees, Dependents
from django.http import HttpResponse


# Create your views here.
def index_page(request):
    return render(request, "index.html")


def get_max_salary_employees(request, top):
    queryset = Employees.objects.all().order_by('-salary')[:top]
    return render(request, "max_salary.html", {"max_salary": queryset})


def get_dependents(request, employee_id):
    queryset = Dependents.objects.all().filter(employee=employee_id)
    employee = Employees.objects.get(employee_id=employee_id)
    context = {"deps": queryset, "employee": employee}
    return render(request, "dependents.html", context)

# def orm_list(request):
#     queryset = Employees.objects.values("job_id").annotate(hodim_soni=Count("*"))
#     # r = list(queryset.employees_set.all())
#     for i in queryset:
#         print(i.last_name)

# print(queryset)
# for i in queryset:
#     print(i)
# return HttpResponse('ok')

# country_list = ""
# for c in queryset:
#     country_list += f"<li>{c.country_name}</li>"
# return HttpResponse(f"<ol>{country_list}</ol>")
