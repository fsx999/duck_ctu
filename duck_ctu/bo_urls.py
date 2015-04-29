from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from duck_inscription.views import UserView, EmailView
import xadmin

xadmin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
                   url(r'^inscription/', include('duck_inscription.urls.adminx_urls')),

                    url(r'^autocomplete/', include('autocomplete_light.urls')),
                    url(r'^compte/', include('duck_inscription.urls.enregistrement_urls')),
                    url(r'^individu/', include('duck_inscription.urls.individu_urls')),
                    url(r'^voeu/', include('duck_inscription.urls.wish_urls')),
                    url(r'^test_user/$', UserView.as_view(), name='test_user'),
                    url(r'^test_email/$', EmailView.as_view(), name='test_email'),
                       url(r'^utils/', include('duck_utils.urls')),
                       url(r'admin/', include(admin.site.urls)),
                       url(r'^', include(xadmin.site.urls)),
                       )

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)), )
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('', (r'^static_tel/(?P<path>.*)$', 'django.views.static.serve',
                                 {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}), )


