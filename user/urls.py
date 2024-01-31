from django.urls import path
from .views import Register,login
urlpatterns = [
    path('register/', Register, name='register'),
    path('login/',login,name='login')
]