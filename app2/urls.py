from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register1, name='r'),
    path('', views.login1, name='l'),
    path('logout/', views.logout, name='l1'),
]