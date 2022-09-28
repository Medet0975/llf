from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class LoginJWTSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(write_only=True)


    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('user email not found')
        return value

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.pop('password', None)

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("not found")
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            refresh = self.get_token(user)

            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)

        return attrs
