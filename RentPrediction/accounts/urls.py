from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.home, name='home_page'),
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    # Add other URL patterns as needed
]
