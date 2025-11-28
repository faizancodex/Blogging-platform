from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('super-admin-portal/', admin.site.urls),
     path('super-secret-admin-panel/', admin.site.urls), 
    path('tinymce/', include('tinymce.urls')),

    
    path('', include('HOME.urls')),
    path('accounts/', include('accounts.urls')),           # for /accounts/*
    path('', include('accounts.profile_urls')),            # for /<username>/

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)