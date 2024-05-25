from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)


# la clase customuser hereda de la clase abstract user de django y 
# agrega un campo name para almacenar el nombre del usuario en la base de datos.
# Sirve para personalizar el modelo de usuario de Django. #