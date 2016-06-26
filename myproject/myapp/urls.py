from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^post/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^post/(?P<post_id>\d+)/delete/$', views.delete, name='delete'),
]
