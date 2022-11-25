from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager): #La forma en que los managers funcionan  es que se espeficican funciones que sirven para poder manipular lo que hay dentro de los objetos
    """manager para perfiles de usuario"""


    def create_user(self, email, name, password=None):
        """crear un nuevo usuario profile"""
        if not email:
            raise ValueError('Usuario debe tener un Email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, username=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

        

class UserProfile(AbstractUser, PermissionsMixin):
    """ modelo base de datos para usuarios en el sistema """
    email = models.EmailField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD =  'email' #Campo de login para el usuario espeficar 
    REQUIRED_FIELDS = ['name'] #Campos requeridos 

    def get_full_name(self):
        """ obtener nombre completo """
        return self.name

    def get_short_name(self):
        """Obtener nombre corto del usuario """
        return self.name

    def __str__(self):
        """retornar cadena de representado nuestro usuario"""
        return self.email
