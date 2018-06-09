from django.conf import settings
from rest_framework import serializers
from member.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    model = MyUser
    fields = (
        'id',
        'password',
        'last_login,',
        'is_superuser'
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'gender',
        'birthday',
    )
    read_only_fields = (
        'id',
        'password',
        'last_login,',
    )
    
    
class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, allow_null=False,)
    password1 = serializers.CharField(write_only=True, allow_null=False, allow_blank=False,)
    password2 = serializers.CharField(write_only=True, allow_null=False, allow_blank=False,)
    first_name = serializers.CharField(allow_blank=True, allow_null=True, default='null',)
    last_name = serializers.CharField(allow_blank=True, allow_null=True, default='null',)
    birthday = serializers.DateField(default='2010-01-01',)
    email = serializers.EmailField(allow_blank=True, allow_null=True, default='null',)
    gender = serializers.ChoiceField(choices=settings.GENDER_CHOICE, default='OTHER')
    agreement = serializers.BooleanField(default=True)
    
    def validate_email(self, email):
        if MyUser.objects.filter(username=email).exists():
            raise serializers.ValidationError('This Email already exist')
        return email

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords didn\'t match')
        return data

    def validate_agreement(self, agreement):
        if not agreement:
            raise serializers.ValidationError("disagreement_fail")
        return agreement
    
    def save(self, *args, **kwargs):
        username = self.validated_data('username', '')
        email = self.validated_data.get('email', '')
        password = self.validated_data.get('password1', '')
        first_name = self.validated_data.get('first_name', '')
        last_name = self.validated_data.get('last_name', '')
        birthday = self.validated_data.get('birthday', '')
        gender = self.validated_data.get('gender', 'OTHER')
        user = MyUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            gender=gender,
        )
        return user