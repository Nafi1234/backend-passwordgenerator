from django.urls import path
from .views import save_password,saved_passwords
urlpatterns = [
    path('api/savepassword/', save_password, name='save'),
    path('api/getpass/',saved_passwords,name='getpass')
]