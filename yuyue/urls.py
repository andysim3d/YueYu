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

from foodplay.controllers.about import About
from foodplay.controllers.blog import Blog
from foodplay.controllers.challenges import Challenges
from foodplay.controllers.home import Home
from foodplay.controllers.join import Join
from foodplay.controllers.shop import Shop
from foodplay.controllers.tips import Tips
from foodplay.controllers.cheesecake import Cheese
from foodplay.controllers.popcake import Popcake

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'home', Home.as_view()),
    url(r'about', About.as_view()),
    url(r'blog', Blog.as_view()),
    url(r'challenges', Challenges.as_view()),
    url(r'shop', Shop.as_view()),
    url(r'tips', Tips.as_view()),
    url(r'join', Join.as_view()),
    url(r'cheese-cake', Cheese.as_view()),
    url(r'popcake', Popcake.as_view()),
    url(r'', Home.as_view()),



]
