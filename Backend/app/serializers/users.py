from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from app.models import Utilisateur
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    # ensuring email is unique
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Utilisateur.objects.all())]
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        required=True,
        write_only=True,
    )

    class Meta:
        model = Utilisateur
        fields = ('first_name', 'last_name', 'email', 'password', 'password2','phone', 'adresse', 'role')
        extra_kwargs = {
            'first_name':{'required':True},
            'last_name':{'required':True},
            'role':{'required':True},
            
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = Utilisateur.objects.create(
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"],
            #birth_date = validated_data["birth_date"],
            phone = validated_data["phone"],
            adresse = validated_data["adresse"],
            role = validated_data["role"],
        )
        # the password is saved this way to be hashed
        user.set_password(validated_data["password"])
        user.save()

        return user