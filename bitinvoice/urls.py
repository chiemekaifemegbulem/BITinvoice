
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

from bitinvoice_01 import views as invoice_views

urlpatterns = [
    path('admin/', admin.site.urls),

    #BITINVOICE URLS
    path('', invoice_views.index, name='index'),
    path('bitinvoice_01/',include('bitinvoice_01.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
