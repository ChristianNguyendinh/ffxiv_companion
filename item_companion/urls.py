from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^all/$', views.all_items),
]