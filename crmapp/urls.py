from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('dash',views.dash,name='dash'),
    path('archive',views.archive,name='archive'),
    
    
]