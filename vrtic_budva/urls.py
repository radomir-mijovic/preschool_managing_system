from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('vrtic.urls')),
    path('', include('companies.urls')),
    path('admin/', admin.site.urls),
]
