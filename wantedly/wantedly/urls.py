"""wantedly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from skills import views as skills_views
from core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
    url(r'^login/$', core_views.login, name="login"),
    url(r'^logout/$', core_views.logout, name="logout"),
    url(r'^users/$', skills_views.user_list, name="user_list"),
    url(r'^endorse/(?P<user_pk>[0-9]+)/(?P<user_profile_pk>[0-9]+)/(?P<skill_set_pk>[0-9]+)/$', skills_views.endorse, name="endorse"),
    url(r'^users/(?P<user_pk>[0-9]+)/(?P<user_profile_pk>[0-9]+)/$', skills_views.user_profile, name="user_profile"),
    url(r'^skills/$', skills_views.skills_list, name="skills_list"),
    url(r'^skills/(?P<skill_pk>[0-9]+)/$', skills_views.skills_users, name="skills_users"),
]
