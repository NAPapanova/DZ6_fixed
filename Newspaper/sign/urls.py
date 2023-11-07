from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, LoginView, LogoutView

app_name = 'sign'
urlpatterns = [
    path('login/',
       LoginView.as_view(template_name='sign/login.html'),
       name='login'),
    path('logout/',
       LogoutView.as_view(template_name='sign/logout.html'),
       name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signup/', RegisterView.as_view(), name='signup')
]