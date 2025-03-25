from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('new/', views.new_technology, name='new_technology'),
    path('contact/', views.contact_view, name='contact'),  # Contact form submission
    path('<str:tech_name>/', views.technology_detail, name='technology_detail'),
]
