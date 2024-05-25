from rest_framework import serializers
from .models import Publication
from django.contrib.auth.models import User


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'