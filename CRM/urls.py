from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shartnoma.views import *

router = DefaultRouter()
router.register('student', StudentViewSet)
router.register('shartnoma', ShartnomaViewSet)
router.register('ustoz', UstozViewSet)
router.register('kurs', KursViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
