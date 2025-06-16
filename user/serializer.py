from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'city', 
                 'state', 'zip_code', 'email', 'password', 'auth_token',
                 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create(**validated_data)


    
