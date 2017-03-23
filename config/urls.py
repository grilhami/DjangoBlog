from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import IndexView
from posts.views import search

from accounts.views import (
    login_view,
    register_view,
    logout_view
)


urlpatterns = [

  # url(r'^$', include("posts.urls", namespace='posts')),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', search , name="search"),
    url(r'^posts/', include("posts.urls", namespace='posts')),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout")

]

if settings.DEBUG:
    urlpatterns += static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
        )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
