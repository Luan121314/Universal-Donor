
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.res_request)
]
