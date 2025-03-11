from django.shortcuts import render
from .models import Kamar, LayananUnggulan

def fasilitas(request):
    # Ambil data dari database jika ada
    kamar_rumah_sakit = Kamar.objects.all()
    layanan_unggulan_db = LayananUnggulan.objects.all()

    # Menyusun daftar fasilitas dan keunggulan manual
    fasilitas = [
        "Unit Gawat Darurat 24 jam dengan penanganan kasus darurat jantung dan stroke",
        "Ruang operasi modern dengan standar internasional",
        "Laboratorium diagnostik lengkap",
        "Fasilitas rawat inap nyaman dengan berbagai kelas",
        "Klinik rawat jalan dengan layanan konsultasi spesialis"
    ]
    
    keunggulan = [
        "Mengutamakan teknologi medis terkini seperti MRI, CT Scan, dan EKG untuk diagnosa cepat dan akurat",
        "Tim dokter spesialis jantung dan saraf berpengalaman lebih dari 10 tahun",
        "Program edukasi kesehatan untuk masyarakat seputar pencegahan penyakit jantung dan stroke"
    ]

    context = {
        'fasilitas': fasilitas,
        'keunggulan': keunggulan,
        'kamar_rumah_sakit': kamar_rumah_sakit,
        'layanan_unggulan_db': layanan_unggulan_db,
    }

    return render(request, 'fasillitas.html', context)


def profil_rumah_sakit(request):
    context = {
        'nama_rumah_sakit': 'Rumah Sakit Sehat Sejahtera',
        'visi': 'Menjadi rumah sakit terkemuka dalam layanan kesehatan spesialis jantung dan saraf yang terpercaya dengan berbasis teknologi modern.',
        'misi': [
            'Memberikan pelayanan kesehatan berkualitas tinggi yang berpusat pada kebutuhan pasien.',
            'Mengembangkan teknologi medis terkini untuk mendukung diagnosa dan perawatan.',
            'Menyediakan tenaga medis dan paramedis profesional serta berpengalaman.',
            'Membangun lingkungan yang nyaman dan aman bagi pasien dan keluarga.',
        ],
    }

    return render(request, 'profile.html', context)
