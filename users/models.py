from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, cnpj, password, **extra_fields):
        if not cnpj:
            raise ValueError('O CNPJ é obrigatório!')
        user = self.model(cnpj=cnpj, username=cnpj, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, cnpj, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(cnpj, password, **extra_fields)
    
    def create_superuser(self, cnpj, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
           raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
           raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(cnpj, password, **extra_fields)

class CustomUser(AbstractUser):
    cnpj = models.CharField('CNPJ', max_length=18, unique=True)
    is_staff = models.BooleanField('Funcionario', default=True)

    USERNAME_FIELD = 'cnpj'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name

    objects = UserManager()