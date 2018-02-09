"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Share.views import HomeView,DisplayView,SearchView,MyView,Phone,ajx
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomeView.as_view(),name="home"),
    url(r'^s/(?P<code>\d+)/$',DisplayView.as_view()),
    url(r'^search/',SearchView.as_view(),name="search"),
    url(r'^my/$',MyView.as_view(),name="MY"),
    url(r'^ajx/', ajx.as_view()),
    url(r'^phone/', Phone.as_view()),
]
