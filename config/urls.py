"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('pybo/', views.index)  # views.py에 index 함수는 구현되지 않은 상태
    path('pybo/',include('pybo.urls'))  #pybo/로 시작하는 페이지 요청은 모두 pybo.urls.py 파일에 있는 URL 매핑을 참고해 처리하라는 의미
]
