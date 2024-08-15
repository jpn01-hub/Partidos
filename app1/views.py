from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response  import Response
from app1.models import Partido, PartidoSerializer


@api_view(['GET'])
def view_Partido(request):
    data  = Partido.objects.all()
    ser = PartidoSerializer(data,many=True)
    rdata = ser.data 

    return Response(rdata)