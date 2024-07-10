from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, FormView
from .forms import ModestContactForm


class ModestTemplView(TemplateView):
    template_name = 'landing/index.html'


class ModestFormView(FormView):
    template_name = 'landing/index.html'  # Шаблон который будет рендерится
    form_class = ModestContactForm  # Класс формы который будет валидироваться
    success_url = '/'  # Ссылка для перехода при удачной валидации

    def form_valid(self, form):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP

        user_agent = request.META.get('HTTP_USER_AGENT')
        return JsonResponse(form.cleaned_data)
