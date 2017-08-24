from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mycart/$', views.mycart, name="mycart"),
    url(r'^create_address$', views.create_address, name="create_address"),
    url(r'^select_address/$', views.select_address, name="select_address"),
]
