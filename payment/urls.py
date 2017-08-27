from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pay/(?P<order_id>[-\w]+)/$', views.pay, name="pay"),
    url(r'^successful_pmt/$', views.successful_pmt, name="successful_pmt"),
    url(r'^unsuccessful_pmt/$', views.unsuccessful_pmt, name="unsuccessful_pmt"),
]
