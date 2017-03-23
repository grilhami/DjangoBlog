from django.conf.urls import url, include
from django.contrib import admin

from .views import (
    PostListView,
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
 
    url(r'^create/$', post_create, name='create'),
    # url(r'^(?P<slg>[\w-]+)/', include([
     url(r'^(?P<pk>\d+)(?:/(?P<slg>[\w\d-]+))?/', include([
        url(
            r'^$',
            post_detail,
            name='detail'),
        url(
            r'^edit/$',
            post_update,
            name='update'),
        url(
            r'^delete/$',
            post_delete,
            name='delete'),
    ])),

]
