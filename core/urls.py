from django.contrib import admin
from django.urls import path
from core import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('produtos/', include('produtos.urls')),
    path('suporte/', views.suporte, name='suporte'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)