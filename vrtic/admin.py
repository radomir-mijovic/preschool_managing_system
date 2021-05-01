from django.contrib import admin
from .models import Kids, Group, Payment, Teachers

admin.site.register(Group)
admin.site.register(Kids)
admin.site.register(Payment)
admin.site.register(Teachers)
