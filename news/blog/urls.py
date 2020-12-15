from django.urls import path
from .views import Home, register_user ,login_user,all_news,logout_user
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', Home, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('news/',all_news,name='all_news'),

]
