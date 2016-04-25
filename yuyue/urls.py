"""yuyue URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from yuyue.about import About
from yuyue.blog import Blog
from yuyue.challenges import Challenges
from yuyue.home import Home
from yuyue.shop import Shop
from yuyue.tips import Tips

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'home', Home.as_view()),
    url(r'about', About.as_view()),
    url(r'blog', Blog.as_view()),
    url(r'challenges', Challenges.as_view()),
    url(r'shop', Shop.as_view()),
    url(r'tips', Tips.as_view()),

]
