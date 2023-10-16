from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

class MahasiswaCreateView(generics.CreateAPIView):
    queryset = mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer
    

