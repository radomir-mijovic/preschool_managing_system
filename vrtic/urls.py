from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'vrtic'

urlpatterns = [
    path('', login_user, name='login'),
    path('logout/', LogoutView.as_view(next_page='vrtic:login'), name='logout'),

    path('kids/', kids_view, name='kids'),
    path('create_kid/', CreateKidView.as_view(), name='create_kid'),
    path('update_kid/<int:pk>/', UpdateKidView.as_view(), name='update_kid'),
    path('delete_kid/<int:pk>/', DeleteKidView.as_view(), name='delete_kid'),

    path('create_payment/<int:pk>/', create_payment, name='create_payment'),
    path('delete_payment/<int:pk>/', delete_payment, name='delete_payment'),
    path('update_payments/<int:pk>/', update_payment, name='update_payments'),
    path('all_paymetns/', all_payments, name='all_payments'),

    path('search', search_bar, name='search'),

    path('groups/', groups_centralni, name='groups_centralni'),
    path('groups_novi/', groups_novi, name='groups_novi'),
    path('groups_tq/', groups_tq, name='groups_tq'),
    path('groups_stefan/', groups_stefan, name='groups_stefan'),
    path('groups_petrovac/', groups_petrovac, name='groups_petrovac'),
    path('group/<int:id>/', group_view, name='group'),

    path('teachers_centralni/', teachers_centralni_view, name='teachers_centralni'),
    path('teachers_novi/', teachers_novi_view, name='teachers_novi'),
    path('teachers_tq/', teachers_tq_view, name='teachers_tq'),
    path('teachers_stefan/', teachers_stefan_view, name='teachers_stefan'),
    path('teachers_petrovac/', teachers_petrovac_view, name='teachers_petrovac'),
    path('teacher_create/', CreateTeacherView.as_view(), name='teacher_create'),
    path('teacher/<int:pk>/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher_delete/<int:pk>/', delete_teacher, name='teacher_delete'),
]
