"""survery_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from apps.form.api.views import FormViewSet

from apps.question.api.views import (
    QuestionOptionViewSet,
    QuestionTypeViewSet,
    QuestionViewSet,
)

router = DefaultRouter()

api_prefix = "api/"
api_ver = "v1/"
context_root = api_prefix + api_ver

router.register(r"question", QuestionViewSet, basename="Question CRUD")
router.register(
    r"question-option", QuestionOptionViewSet, basename="Question Option CRUD"
)
router.register(r"question-type", QuestionTypeViewSet, basename="Question Type CRUD")
router.register(r"form", FormViewSet, basename="Form CRUD")


urlpatterns = [
    path(context_root + "admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls

admin.site.site_header = "Interrogatio Responsio Admin"
admin.site.site_title = "Interrogatio Responsio Admin Portal"
admin.site.index_title = "Welcome to Interrogatio Responsio Portal"
