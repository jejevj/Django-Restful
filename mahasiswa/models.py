from django.db import models

# Create your models here.

    
class mahasiswa(models.Model): 
    nim = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    kelas = models.CharField(max_length=1)
    created_at = models.DateField(auto_now=True)  