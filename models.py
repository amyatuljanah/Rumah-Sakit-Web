from django.db import models

class LayananUnggulan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama



class Kamar(models.Model):
    nama = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='kamar_images/')
    kelas = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

