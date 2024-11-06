from django.urls import path
from . import views

urlpatterns = [
    path("",views.Users.as_view()),
    path('me', views.Me.as_view()),
    path('change-password',views.ChangePassword.as_view()),
    path('@<str:username>',views.PublicUser.as_view()), # @를 쓰는이유는 me라는 이름을 가진 사람이 있을 수 있기때문에.
]
