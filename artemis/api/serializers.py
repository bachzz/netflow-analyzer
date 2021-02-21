from rest_framework import serializers
from .models import test_model

class test_model_serializers(serializers.ModelSerializer):
    class Meta:
        model = test_model
        fields = '__all__'