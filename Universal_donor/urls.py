
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.res_request),
    path('cadastro/',views.cadastro, name='cadastro'),
    path('login/',views.login, name='login'),


]
