# Generated by Django 5.1.3 on 2024-11-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasilitas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kamar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('gambar', models.ImageField(upload_to='kamar_images/')),
                ('kelas', models.CharField(max_length=50)),
            ],
        ),
    ]
