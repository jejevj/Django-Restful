from .models import *
from rest_framework import serializers as sz

class MahasiswaSerializer(sz.ModelSerializer):
    class Meta:
        model = mahasiswa
        fields = '__all__'