from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^demos/$', views.demo, name='demo'),
    url(r'^contact/$', views.contact, name='contact'),
]