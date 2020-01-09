"""
Definition of urls for DjangoWebProject2.
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('', include('cineseries.urls')),
    path('admin/', admin.site.urls),
    path('cineseries/', include('cineseries.urls')),
    # Examples:
    # url(r'^$', DjangoWebProject2.views.home, name='home'),
    # url(r'^DjangoWebProject2/', include('DjangoWebProject2.DjangoWebProject2.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


