from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CertificadoViewSet, DatoPersonalViewSet, ExperienciaViewSet,
    ProyectoViewSet, RedSocialViewSet, SkillViewSet, UsuarioAdminViewSet
)

router = DefaultRouter()
router.register(r'certificados', CertificadoViewSet)
router.register(r'datos-personales', DatoPersonalViewSet)
router.register(r'experiencias', ExperienciaViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'redes-sociales', RedSocialViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'usuarios-admin', UsuarioAdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
