from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    ]