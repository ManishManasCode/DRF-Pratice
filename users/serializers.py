from django.contrib.auth import get_user_model 
from rest_framework import serializers 



class StudentUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]
    

    def create(self, validated_data):
        get_user_model().objects.create_student(**validated_data)
        return validated_data
