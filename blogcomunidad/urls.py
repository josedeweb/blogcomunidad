from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from blog import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<slug>[^/]+)/$', views.PostView.as_view(), name='post'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
