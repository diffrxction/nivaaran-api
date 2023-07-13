from rest_framework import serializers

from login.models import Organisation

class OrganisationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"
        depth=2