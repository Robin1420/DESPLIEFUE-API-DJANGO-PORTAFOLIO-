from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import (
    Proyectos, RedesSociales, Skills, UsuariosAdmin,
    Certificados, DatosPersonales, Experiencias
)
from .serializers import (
    ProyectoSerializer, RedSocialSerializer, SkillSerializer, UsuarioAdminSerializer,
    CertificadoSerializer, DatoPersonalSerializer, ExperienciaSerializer
)


class CertificadoViewSet(viewsets.ModelViewSet):
    queryset = Certificados.objects.all()
    serializer_class = CertificadoSerializer
    permission_classes = [AllowAny]


class DatoPersonalViewSet(viewsets.ModelViewSet):
    queryset = DatosPersonales.objects.all()
    serializer_class = DatoPersonalSerializer
    permission_classes = [AllowAny]


class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencias.objects.all()
    serializer_class = ExperienciaSerializer
    permission_classes = [AllowAny]


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [AllowAny]


class RedSocialViewSet(viewsets.ModelViewSet):
    queryset = RedesSociales.objects.all()
    serializer_class = RedSocialSerializer
    permission_classes = [AllowAny]


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]


class UsuarioAdminViewSet(viewsets.ModelViewSet):
    queryset = UsuariosAdmin.objects.all()
    serializer_class = UsuarioAdminSerializer
    permission_classes = [AllowAny]
