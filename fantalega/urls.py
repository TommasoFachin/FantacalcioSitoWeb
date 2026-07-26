from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('storia/', views.storia, name='storia'),
    path('regolamento/', views.regolamento, name='regolamento'),
    path('rose/', views.rose, name='rose'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Per login, logout, etc.
    path('pagamenti/', include(('apps.payments.urls', 'payments'), namespace='payments')),
    path('teams/', include(('apps.teams.urls', 'teams'), namespace='teams')),
    path('media/', include(('apps.media.urls', 'media'), namespace='media')),
    path('trophies/', include(('apps.trophies.urls', 'trophies'), namespace='trophies')),
]

# Aggiunta per servire i file media in modalità DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)