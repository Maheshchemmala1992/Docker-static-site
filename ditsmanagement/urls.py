from django.conf import settings
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.views.static import serve
# from django.conf.urls import url


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    
    path('attendance/',include('attendance.urls')),

    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
