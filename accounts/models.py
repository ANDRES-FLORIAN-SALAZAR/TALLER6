# models.py
from django.db import models
import json
from django.contrib.auth import get_user_model

# Modelo para registrar logs de inserciones de usuarios
class UsuariosInsertLog(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Relación con el usuario
    username = models.CharField(max_length=150)  # Nombre de usuario
    email = models.EmailField()  # Correo electrónico
    first_name = models.CharField(max_length=30, blank=True, null=True)  # Primer nombre
    last_name = models.CharField(max_length=150, blank=True, null=True)  # Apellido
    date_joined = models.DateTimeField()  # Fecha de registro
    operation_type = models.CharField(max_length=10, default='INSERT')  # Tipo de operación
    operation_timestamp = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la operación
    operation_user = models.CharField(max_length=150, blank=True, null=True)  # Usuario que realizó la operación

    # Meta información para el modelo, define nombres legibles en la interfaz de administración
    class Meta:
        verbose_name = 'Log de Inserciones'  # Nombre singular
        verbose_name_plural = 'Logs de Inserciones'  # Nombre plural

    # Representación en cadena del objeto para facilitar su identificación
    def __str__(self):
        return f"INSERT {self.username} at {self.operation_timestamp}"


# Modelo para registrar logs de actualizaciones de usuarios
class UsuariosUpdateLog(models.Model):
    user_id = models.IntegerField()  # ID del usuario
    changed_fields = models.JSONField()  # Campos modificados
    old_values = models.JSONField(blank=True, null=True)  # Valores antiguos
    new_values = models.JSONField(blank=True, null=True)  # Nuevos valores
    operation_type = models.CharField(max_length=10, default='UPDATE')  # Tipo de operación
    operation_timestamp = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la operación
    operation_user = models.CharField(max_length=150, blank=True, null=True)  # Usuario que realizó la operación

    # Meta información para el modelo, define nombres legibles en la interfaz de administración
    class Meta:
        verbose_name = 'Log de Actualizaciones'  # Nombre singular
        verbose_name_plural = 'Logs de Actualizaciones'  # Nombre plural

    # Representación en cadena del objeto para facilitar su identificación
    def __str__(self):
        return f"UPDATE user {self.user_id} at {self.operation_timestamp}"

    # Método para obtener una lista de los campos modificados
    def get_changed_fields_display(self):
        return ", ".join(json.loads(self.changed_fields).keys())


# Modelo para registrar logs de eliminaciones de usuarios
class UsuariosDeleteLog(models.Model):
    user_id = models.IntegerField()  # ID del usuario
    username = models.CharField(max_length=150)  # Nombre de usuario
    email = models.EmailField()  # Correo electrónico
    first_name = models.CharField(max_length=30, blank=True, null=True)  # Primer nombre
    last_name = models.CharField(max_length=150, blank=True, null=True)  # Apellido
    date_joined = models.DateTimeField()  # Fecha de registro
    operation_type = models.CharField(max_length=10, default='DELETE')  # Tipo de operación
    operation_timestamp = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la operación
    operation_user = models.CharField(max_length=150, blank=True, null=True)  # Usuario que realizó la operación

    # Meta información para el modelo, define nombres legibles en la interfaz de administración
    class Meta:
        verbose_name = 'Log de Eliminaciones'  # Nombre singular
        verbose_name_plural = 'Logs de Eliminaciones'  # Nombre plural

    # Representación en cadena del objeto para facilitar su identificación
    def __str__(self):
        return f"DELETE {self.username} at {self.operation_timestamp}"