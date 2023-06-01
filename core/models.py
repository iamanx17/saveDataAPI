from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils import timezone
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.


class Usermanager(BaseUserManager):
    def create_user(self, email , password, **extra_fields):

        if not email:
            raise ValueError("email is a required field")
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')

        user= self.create_user(email, password, **extra_fields)
        return user

class Users(AbstractUser):
    user_name = models.CharField("Username",max_length=250, unique= True)
    email = models.EmailField('Email Address', unique= True)
    first_name = models.CharField("First Name",max_length=250, null= True)
    last_name = models.CharField("Last Name", max_length=50, null= True)
    phone = models.CharField(validators=[MaxLengthValidator(10), MinLengthValidator(10)], null=True, max_length=10)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = Usermanager()

    def __str__(self):
        return self.email
    


class saveData(models.Model):
    id = models.AutoField(primary_key= True)
    key = models.CharField(max_length=250, unique= True)
    value = models.JSONField()
    note = models.CharField("Note (Optional Field)", max_length=250, null= True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey("Users", verbose_name="user", on_delete=models.CASCADE)

    def __str__(self):
        return self.key + ' ' + str(self.note)