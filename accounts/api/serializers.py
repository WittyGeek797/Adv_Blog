from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError,
    EmailField,
    CharField
)

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from django.db.models import Q


User = get_user_model()


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user is already registered")
        return data

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match")
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user is already registered")
        return value

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match")
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user is already registered")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True, label='Username')
    email = EmailField(label='Email Address',required=False, allow_blank=True,)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A Username or Email is required to login.")
        user = User.objects.filter(
                Q(email=email) |
                Q(username=username) 
            ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='') #For users with null email id
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This Username/Email is not valid")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect Credentials entered.")
        data["token"] = "SOME RANDOM TOKEN"
        return data
