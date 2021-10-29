from rest_framework import serializers
from .models import LibrarySet

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrarySet
        fields = '__all__'
