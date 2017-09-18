from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from Tagent.views import *
router = routers.DefaultRouter()
router.register(r'customers',CustomerViewSet)
router.register(r'address',CustomerAddressViewSet)
router.register(r'agents',AgentViewSet)
router.register(r'address',AgentAddressViewSet)
router.register(r'agentreferal',AgentReferalViewSet)
router.register(r'location',LocationViewSet)
router.register(r'propertytype',PropertyTypeViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('Tagent.urls')),
url(r'^', include(router.urls)),
]

