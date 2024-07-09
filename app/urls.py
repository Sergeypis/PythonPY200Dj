from django.urls import path
from .views import template_view, index_view, login_view, register_view, \
    logout_view, user_detail_view, get_text_json

from .views import TemplView, MyTemplView


app_name = 'app'

urlpatterns = [
    path('', index_view, name='index'),
    path('template/', MyTemplView.as_view(), name='template'),
    path('template/', TemplView.as_view(), name='template'),
    path('template/', template_view, name='template'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('profile/', user_detail_view, name='user_profile'),
    path('get/text/', get_text_json),
]