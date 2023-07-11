from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from nivaaranapp.models import MLModels
from nivaaranapp.serialisers import MlModelSerialiser
# Create your views here.
class Index(APIView):
    def get(self,request):
        return Response(
            {
                'data':"OKK"
            },
            status=status.HTTP_202_ACCEPTED
        )
    
class GetModels(APIView):
    def get(self,request):
        db = MLModels.objects.filter(type=request.GET['type'])
        data = MlModelSerialiser(db,many=True)
        return Response(
            {
                "models":data.data
            }
        )