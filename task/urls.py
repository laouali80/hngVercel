from django.urls import path
from . import views


urlpatterns = [
    path('', views.test, name='test'),
    # path('', views.welcome, name='welcome'),
    # path('api/hello', views.api, name='api'),
]