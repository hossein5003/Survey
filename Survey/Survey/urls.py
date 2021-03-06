"""Survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from account.views import LogInView, LogOutView, SignUpView, ActivateView
from main.views import CreateSurvey, CreateQuestion

urlpatterns = [
    path('admin/', admin.site.urls),

    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('activate/', ActivateView.as_view(), name='activate'),

    path('survey/create/', CreateSurvey.as_view(), name='create'),
    path('create/question/', CreateQuestion.as_view(), name='create_question'),
]
