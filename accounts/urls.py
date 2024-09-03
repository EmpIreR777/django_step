from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView, CustomLoginView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        'login/',
        CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
