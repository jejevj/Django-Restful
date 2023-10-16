from django.urls import path
from . import views, createview

urlpatterns =[
    # Default
    path('',views.home,name="Home"),
    
    # MAHASISWA ENDPOINT
    path('mahasiswa/',views.getMahasiswa),
    path('store-mahasiswa',createview.MahasiswaCreateView.as_view(),name="Mahasiswa POST"),
    
]