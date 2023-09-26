from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed

CustomUser = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    college_id = serializers.CharField(max_length=10)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        college_id = data.get('college_id')
        password = data.get('password')

        user = CustomUser.objects.filter(username=username, college_id=college_id).first()

        if user is None or not user.check_password(password):
            raise AuthenticationFailed('Invalid username, college ID, or password.')

        return user

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'college_id', 'password', 'name', 'description', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            college_id=validated_data['college_id'],
            name=validated_data.get('name', ''),  
            description=validated_data.get('description', ''),  
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
