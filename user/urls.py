from django.urls import path
from django.contrib.auth import views as auth_views

from core.forms import LoginForm
from . import views

app_name = 'user'

urlpatterns = [
     path('login/',auth_views.LoginView.as_view(authentication_form=LoginForm,template_name='user/login.html'),name='login'),
     path('sigin/',views.signIn,name='signin'),
     path('logout/',views.userLogout,name='logout')
#      path('ac')
]