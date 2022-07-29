#Импорт CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

#Функция reverse_lazy позволяет получить URL по параметрам ф-ции path()
from django.urls import reverse_lazy

#Импортиуем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm 


class SignUp(CreateView):
    form_class = CreationForm
    #перенаправление на главную страницу после успешной регистрации
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'