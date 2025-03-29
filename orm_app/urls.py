from django.urls import path
from .views import index_page, get_max_salary_employees, get_dependents
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index_page, name='orm_lis'),
    path('salary/<int:top>', get_max_salary_employees, name='employee-list'),
    path('deps/<int:employee_id>', get_dependents, name='deps-list'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urlpatterns = [
#     path('',orm_list, name='orm_list'),
# ]
