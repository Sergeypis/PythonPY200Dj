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

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP
        user_agent = request.META.get('HTTP_USER_AGENT')

        new_context = {'ip': ip, 'user_agent': user_agent}

        form = self.get_form()
        if form.is_valid():
            context = self.form_valid(form)
            context.update(new_context)
            return JsonResponse(context)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return form.cleaned_data



