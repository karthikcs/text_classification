"""getsentiment URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path , include
from sentiapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': "users/registration/login.html"}, name='login'),
    # url(r'^logout/$', auth_views.LogoutView, name='logout'),
    url(r'^sentiment/', getsentenceView),
    url(r'^add/',addSentenceView),
    url(r'^retrain/', retrainView),
    path('updatesenti/<int:i>/',updatesentiView),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', HomePageView.as_view(), name='home'),
    path('', getsentenceView, name='home'),
]

# _model = fasttext.load_model("model_senti.bin")