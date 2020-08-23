"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

import sys
from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    # http://localhost:8000/
    # path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    # path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    # path('api/admin/', admin.site.urls),

    url(r'^', include('backend.core.urls')),
]

if 'runserver' in sys.argv:
    # start scheduler
    from backend.core.scheduler import sm

    # sm.start()
