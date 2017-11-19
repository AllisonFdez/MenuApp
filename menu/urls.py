from django.conf.urls import url
from django.contrib.auth.views import login
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^menu/', views.menu, name='menu'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^login/', login, {'template_name':'login.html'}, name='login'),
]