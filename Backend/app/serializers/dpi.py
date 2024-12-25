from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from app.models import Utilisateur, DPI
from django.contrib.auth.password_validation import validate_password

# Nested serializer for DPI
class DPISerializer(serializers.ModelSerializer):
    nss = serializers.CharField(
        max_length=30,
        required=True,
        validators=[UniqueValidator(queryset=DPI.objects.all())]
    )
    mutuelle = serializers.CharField(max_length=100, required=True)
    contact_info = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = DPI
        fields = ('nss', 'mutuelle', 'contact_info')

# Main serializer
class AddDPISerializer(serializers.ModelSerializer):
    # Fields for Utilisateur
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
    dpi_input = DPISerializer()  # Nested DPI serializer

    class Meta:
        model = Utilisateur
        fields = ['first_name', 'last_name', 'email', 'password', 'password2', 'phone', 'adresse', 'role', 'dpi_input']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'role': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        if attrs['role'] != 'patient':
            raise serializers.ValidationError({"other user can be created at /users/add"})
        return attrs

    def create(self, validated_data):
        # Extract DPI data
        dpi_data = validated_data.pop('dpi_input')

        # Create user
        user = Utilisateur.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            phone=validated_data["phone"],
            adresse=validated_data["adresse"],
            role=validated_data["role"],
        )
        user.set_password(validated_data["password"])
        user.save()

        # Create related DPI
        DPI.objects.create(
            nss=dpi_data['nss'],
            mutuelle=dpi_data['mutuelle'],
            contact_info=dpi_data['contact_info'],
            user=user
        )

        return user
