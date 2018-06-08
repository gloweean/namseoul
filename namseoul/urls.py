"""namseoul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from message import views
from rest_framework import routers
from rest_framework.authtoken import views as AuthView
from member.views import UserLogoutView

# ViewSet을 사용할 경우 router를 지정해주어야 한다.
router = routers.DefaultRouter()
router.register(r'message', views.MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth', AuthView.obtain_auth_token),  # 이후 요청부터는 Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b 형식으로 request header에 넣어서 요청을 보내야 한다.
    path('logout', UserLogoutView.as_view()),
]
