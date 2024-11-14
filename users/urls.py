from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("",views.Users.as_view()),
    path('me', views.Me.as_view()),
    path('change-password',views.ChangePassword.as_view()),
    path('log-in', views.LogIn.as_view()),
    path('log-out', views.LogOut.as_view()),
    path('token-login', obtain_auth_token),
    path('@<str:username>',views.PublicUser.as_view()), # @를 쓰는이유는 me라는 이름을 가진 사람이 있을 수 있기때문에.
]
