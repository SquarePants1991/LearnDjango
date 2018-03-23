from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
    path('<int:student_id>/score/', views.score_detail, name='score_detail'),
]