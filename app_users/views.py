
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from app_users.forms import AuthForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


def login_view(request):
    if request.method == 'POST': #для POST запроса пытаемся аутентифицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            user_name = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main.html')
                else:
                    auth_form.add_error('__all__', 'Ошибка, учетная запись пользователя не активна!')
            else:
                auth_form.add_error('__all__', 'Ошибка, проверьте правильность написания логина и пароля')
    else:    #При остальных видов запроса отображаем страницу запроса
        auth_form = AuthForm()
        context = {
            'form' : auth_form
        }
    return render(request, 'login.html', context=context)


class MainView(View):
    
    def get(self, request):
        return render(request, 'main.html')


class AnotherLoginView(LoginView):
    template_name = 'login.html'
    
class AnotherLogoutview(LogoutView):
    #template_name = 'logout.html'
    next_page = '/'    

def logout_view(request):
    logout(request)
    return HttpResponse('ВЫход из учетной записи прошел успешно')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form' : form})


def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth = date_of_birth
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form' : form})