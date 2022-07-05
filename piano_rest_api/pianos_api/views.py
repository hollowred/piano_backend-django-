from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import PianoSerializer
from .models import Piano

class PianoList(generics.ListCreateAPIView):
    queryset = Piano.objects.all().order_by('id
    serializer_class = PianoSerializer

class PianoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Piano.objects.all().order_by('id')
    serializer_class = PianoSerializer    
