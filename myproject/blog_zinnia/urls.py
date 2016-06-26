from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^entry/(?P<pk>\d+)/(?P<date>\d+)/(?P<slug>[-\w]+)/$', views.entry_detail, name='entry_detail'),
    url(r'^author/(?P<author>[-\w]+)/$', views.author_detail, name='author_detail'),
]
