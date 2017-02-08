from django.conf.urls import url
from . import views

app_name = 'general'
urlpatterns = [
    url(r'^$', views.TopView.as_view(), name="top"),
]