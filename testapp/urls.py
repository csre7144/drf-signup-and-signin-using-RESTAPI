from django.urls import path
from . import views
from .views import UserListCreateAPIView


urlpatterns = [
    path('register/',views.home, name='home'),
    path('homepage/',views.homepage, name='homepage'),
    path('',views.signin_list, name='signin_list'),
    path('userlogin/', UserListCreateAPIView.as_view(), name='userlogin'),
    path('logout_view/', views.logout_view, name='logout_view'),
]
