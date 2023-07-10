from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class Index(APIView):
    def get(self,request):
        return Response(
            {
                'data':"OK"
            },
            status=status.HTTP_202_ACCEPTED
        )