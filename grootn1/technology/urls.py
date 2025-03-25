from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('new/', views.new_technology, name='new_technology'),
    path('contact/', views.contact_view, name='contact'),  # Contact form submission

    # Keep this at the end to avoid conflicts with predefined paths
    path('<str:tech_name>/', views.technology_detail, name='technology_detail'),
]
