from django.urls import path

from .views import ModestTemplView, ModestFormView


app_name = 'landing'

urlpatterns = [
    path('modest_template/', ModestFormView.as_view(), name='modest_template'),
    path('modest_template/', ModestTemplView.as_view(), name='modest_template'),
]