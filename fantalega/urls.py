from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('storia/', views.storia, name='storia'),
    path('chi-siamo/', views.chi_siamo, name='chi_siamo'),
    path('regolamento/', views.regolamento, name='regolamento'),
    # Modificato: ora punta alla pagina di selezione dell'anno
    path('rose/', views.rose_home, name='rose_home'),
    # Aggiunto: nuovo URL per visualizzare le rose di un anno specifico
    path('rose/<str:year>/', views.rose, name='rose_detail'),
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