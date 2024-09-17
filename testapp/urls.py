from django.urls import path
from . import views
# from .views import UserListCreateAPIView


urlpatterns = [
    path('register/',views.home, name='home'),
    path('homepage/',views.homepage, name='homepage'),
    path('',views.signin_list, name='signin_list'),

    # Class-based views
    # path('userlogin/', UserListCreateAPIView.as_view(), name='userlogin'),

    # @APiView
    path('UserListCreate/', views.UserListCreate),
    path('UserListCreate/<int:pk>', views.UserListCrud),
    path('logout_view/', views.logout_view, name='logout_view'),
]
