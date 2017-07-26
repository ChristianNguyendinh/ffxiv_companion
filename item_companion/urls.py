from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^item/(?P<itemname>\w{,50})/$', views.single_item),
	url(r'^item-names/$', views.all_item_names),
	url(r'^item-full/$', views.all_item_full),
]