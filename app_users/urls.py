from django.urls import path

from .views import AnotherLoginView, another_register_view, login_view, logout_view, register_view



urlpatterns = [
    path('login', login_view, name='login'),
    path('another_login', AnotherLoginView.as_view()),
    path('logout', logout_view, name = 'logout'),
    path('another_logout', AnotherLoginView.as_view()),
    path('register', register_view, name='register'),
    path('another_register', another_register_view, name = 'another_register' )
]
