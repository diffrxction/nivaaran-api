from rest_framework import serializers

from nivaaranapp.models import MLModels
from nivaaransite.settings import PROJECT_URL

class MlModelSerialiser(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = MLModels
        fields = "__all__"

    def get_file(self,obj):
        return PROJECT_URL + obj.file.url