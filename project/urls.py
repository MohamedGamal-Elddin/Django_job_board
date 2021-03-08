from django.contrib import admin
from django.urls import path, include

from django.conf import settings           # becouse static files and media fieles
from django.conf.urls.static import static # becouse static files and media fieles

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.accounts_url',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('jobs/',include('job.job_url',namespace='jobs')),
    path('contact/',include('contact.contact_url',namespace='contact')),
    path('api-auth/', include('rest_framework.urls')),

    
            ]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)