from django.urls import path
from . import views

urlpatterns = [
    path('api/pianos', views.PianoList.as_view(), name='piano_list'),
    path('api/pianos/<int:pk>', views.PianoDetail.as_view(), name='piano_detail'),
]    
