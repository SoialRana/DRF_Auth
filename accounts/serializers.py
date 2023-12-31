 

from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email','username', 'password', 'confirm_password']
        extra_kwargs={
        'password':{'write_only':True}
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match!")

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number')



class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    class Meta:
        model=User
        fields=['email','password']
    

    
    
