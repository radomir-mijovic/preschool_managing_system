from django.urls import path
from .views import *

app_name = 'companies'

urlpatterns = [

    path('companies/', index_view, name='index'),
    path('create_company/', CreateCompanyView.as_view(), name='create_company'),
    path('delete_company/<int:pk>/', DeleteCompanyView.as_view(), name='delete_company'),
    path('update_company/<int:pk>/', UpdateCompanyView.as_view(), name='update_company'),

    path('company_payment/<int:pk>/', company_payment, name='company_payment'),
    path('update_company_payments/<int:pk>/', update_company_payments, name='update_company_payments'),
    path('delete_payment_company/<int:pk>/', delete_payment_company, name='delete_payment_company'),

    path('search_result/', search_company, name='search_company')

]
