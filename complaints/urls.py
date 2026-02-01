from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_complaint, name='create_complaint'),
    path('my/', views.my_complaints, name='my_complaints'),
    path('all/', views.all_complaints, name='all_complaints'),
]
