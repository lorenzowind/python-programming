from django.db import models
from django.core.validators import EmailValidator, validate_ipv4_address
from django.core.exceptions import ValidationError

def validate_password_length(value, length=8):
    if len(str(value)) < length:
        raise ValidationError('Password not allowed')

def validate_level_choices(value):
    if value not in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']:
        raise ValidationError('Level not allowed')

class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateField(auto_now=True, auto_now_add=False)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50, validators=[validate_password_length])

class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(max_length=39, protocol="IPv4")

class Event(models.Model):
    level = models.CharField(max_length=20, validators=[validate_level_choices])
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateField(auto_now=True, auto_now_add=False)
    
    agent = models.ForeignKey(Agent, on_delete=models.deletion.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE, blank=True)

class Group(models.Model):
    name = models.CharField(max_length=50)

class GroupUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.deletion.CASCADE, null=True, blank=True)
