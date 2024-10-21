from django.urls import path
from . import views

urlpatterns = [
    path('puzzle/', views.puzzle, name='puzzle'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
]
