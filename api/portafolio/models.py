# -*- coding: utf-8 -*-
from django.db import models


class Certificados(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    institucion = models.CharField(max_length=150, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    imagen = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificados'


class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    profesion = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    foto_perfil = models.CharField(max_length=100, blank=True, null=True)
    cv = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_personales'


class Experiencias(models.Model):
    puesto = models.CharField(max_length=150, blank=True, null=True)
    empresa = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    actual = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiencias'


class Proyectos(models.Model):
    titulo = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tecnologias = models.CharField(max_length=500, blank=True, null=True)
    imagen = models.CharField(max_length=100, blank=True, null=True)
    enlace_demo = models.CharField(max_length=300, blank=True, null=True)
    enlace_codigo = models.CharField(max_length=300, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyectos'


class RedesSociales(models.Model):
    plataforma = models.CharField(max_length=50, blank=True, null=True)
    enlace = models.CharField(max_length=300, blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redes_sociales'


class Skills(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'


class UsuariosAdmin(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password_hash = models.CharField(max_length=300)
    email = models.CharField(max_length=150, blank=True, null=True)
    creado_en = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_admin'
