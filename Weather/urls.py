from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#index url
    url(r'^info/$', views.info, name='info'),#result url
]
