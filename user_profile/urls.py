from django.urls import path
from user_profile.views import UserFormView, UserEditFormView

urlpatterns = [
    path('register', UserFormView.as_view(), name = 'Форма регистрации'),
    path('<int:profile_id>/edit', UserEditFormView.as_view())
]
