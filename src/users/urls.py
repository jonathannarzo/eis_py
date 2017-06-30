from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import forms, views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name':'users/login.html','authentication_form':forms.AppLogin}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'home.html'}, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^create/$', views.create_user, name='create'),
    url(r'^list/$', views.list_users, name='list'),
    url(r'^roles/$', views.create_role, name='roles'),
]
