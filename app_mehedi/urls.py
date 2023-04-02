from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('signout/', views.signout, name='signout'),
    path('nature/', views.nature, name='nature'),
    path('animal/', views.animal, name='animal'),
    path('portrait/', views.portrait, name='portrait'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),

    
]