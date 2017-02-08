from django.conf.urls import url
from . import views

app_name = 'general'
urlpatterns = [
    url(r'^$', views.TopView.as_view(), name="top"),
    url(r'^product/$', views.ProductView.as_view(), name="product"),
]