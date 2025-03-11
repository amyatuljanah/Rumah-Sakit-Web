from django.contrib import admin
from django.urls import path
from fasilitas import views as ujianviews  # Mengimpor views dari aplikasi 'fasilitas'
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ujianviews.profil_rumah_sakit, name='profil'),  # Profil Rumah Sakit
    path('fasilitas/', ujianviews.fasilitas, name='fasilitas')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Menambahkan dukungan untuk file media
