from django.urls import path
from .views import register, signin, home, profile, signout
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', signin, name='signin'),
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('logout/', signout, name='logout'),
]
