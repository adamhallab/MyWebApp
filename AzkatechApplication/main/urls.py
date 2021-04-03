from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("add/", views.add, name= "add"),
    path('update/<int:pk>/', views.VacationUpdate, name='vac_update'),
    path('delete/<int:pk>/', views.VacationDelete, name='vac_delete'),
]