from rest_framework import serializers
from .models import (
    Proyectos, RedesSociales, Skills, UsuariosAdmin,
    Certificados, DatosPersonales, Experiencias
)


class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificados
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

class DatoPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosPersonales
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencias
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyectos
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'fecha': {'read_only': True}
        }


class RedSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedesSociales
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class UsuarioAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosAdmin
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'creado_en': {'read_only': True}
        }

    def create(self, validated_data):
        # Aquí podrías agregar lógica personalizada para crear usuarios
        return super().create(validated_data)
