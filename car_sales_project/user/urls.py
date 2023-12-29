from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.UserLoginView.as_view(), name="loginView"),
    path('logout/',views.UserLogoutView.as_view(), name="logoutView"),
    path('reg/',views.regestrations, name="regestration"),
    path('profile/',views.ProfleView.as_view(), name="profile"),
    # path('change_profile/',views.ChangeProfileInfo, name="changeprofile"),
    path('change_profile/',views.ChangeProfileView.as_view(), name="changeprofile"),
]