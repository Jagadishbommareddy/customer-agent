from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'agent/add/$', views.AgentAddrLocArefCreate.as_view(), name='agent-add'),
    url(r'agent/(?P<pk>[0-9]+)/$', views.AgentAddrLocArefUpdate.as_view(), name='agent-update'),
    url(r'agent/(?P<pk>[0-9]+)/delete/$', views.AgentDelete.as_view(), name='agent-delete'),
    url(r'^$', views.AgentList.as_view(), name='agent-list'),

    url(r'^$', views.CustomerList.as_view(), name='customer-list'),
    url(r'customer/add/$', views.CustomerAddressCreate.as_view(), name='customer-add'),
    url(r'customer/(?P<pk>[0-9]+)/$', views.CustomerAddressUpdate.as_view(), name='customer-update'),
    url(r'customer/(?P<pk>[0-9]+)/delete/$', views.CustomerDelete.as_view(), name='customer-delete'),


]