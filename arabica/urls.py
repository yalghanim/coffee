from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^signup/$', views.usersignup, name="signup"),
    url(r'^login/$', views.userlogin, name="login"),
    url(r'^logout/$', views.userlogout, name="logout"),
    url(r'^order/$', views.order, name="order"),
    url(r'^rbsp/$', views.rbsp, name="rbsp"),
    url(r'^list/$', views.orderlist, name="list"),
    url(r'^adminlist/$', views.adminlist, name="adminlist"),
    url(r'^address/$', views.address, name="address"),
    url(r'^detail/(?P<order_id>[-\w]+)/$', views.orderdetail, name="detail"),
    url(r'^update/(?P<order_id>[-\w]+)/$', views.update, name="update"),
    url(r'^delete/(?P<order_id>[-\w]+)/$', views.delete, name="delete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

