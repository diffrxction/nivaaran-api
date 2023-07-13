from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from login.models import Organisation
from login.serialisers import OrganisationSerialiser
class Login(APIView):
    def post(self,request):
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        db = Organisation.objects.filter(user__email=email)
        if db.exists():
            auth = authenticate(username=db.first().user.username,password=password)
            if auth is not None:
                data = OrganisationSerialiser(db.first())
                return Response(
                    {
                        "login":True,
                        "status":200,
                        'credentials':data.data
                    },status=status.HTTP_200_OK
                )
        return Response(
            {
                "message":"OK"
            },
            status=status.HTTP_200_OK
        )