import debug_toolbar

from django.conf.urls import include, url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^test/', views.test, name='test'),
]
