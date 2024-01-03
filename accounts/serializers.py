 
from rest_framework import serializers
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    # We are writing this because we need confirm password field in our registration request
    confirm_password = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email','username', 'password', 'confirm_password']
        extra_kwargs={
        'password':{'write_only':True}
        }

    # Validating password and confirm password while registration 
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match!")

        return data

    def create(self, validated_data): 
        # when we use userserializer
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
        # return User.objects.create_user(**validated_data) # When we use login serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number','email')



class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    class Meta:
        model=User
        # fields=('first_name', 'last_name', 'phone_number','email','password')
        fields=('first_name','email','password')
    

    
    
