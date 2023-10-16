from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

# home
def home(request):
    return render(request,"home.html")
    
#Error 404
def custom_404(request, exception):
    return render(request, 'home.html', status=404)

@api_view(['GET'])
def getMahasiswa(request):
    matkul = mahasiswa.objects.all()
    serializer = MahasiswaSerializer(matkul, many=True)
    return Response(serializer.data)