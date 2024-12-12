from django.urls import path,include
from .views import sign_up,login,dashboard,logout

urlpatterns = [
    path('',sign_up,name='signup'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),  
  
]