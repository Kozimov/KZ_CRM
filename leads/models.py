from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

class Lead(models.Model):
    ismi = models.CharField(max_length=20)
    familiyasi = models.CharField(max_length=20)
    yoshi = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ismi)
        

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profil = models.ForeignKey(UserProfil, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

def post_user_create(sender, instance, created, **kwargs):
    if created:
        UserProfil.objects.create(user=instance) 

post_save.connect(post_user_create, sender=User)