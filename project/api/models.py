from django.db import models

# Create your models here.
class UserModel(models.Model):
    
    class UserTypes(models.TextChoices):
        CLIENT        = "client"
        PROFESSIONAL =  "careprovider"

    user_id   = models.CharField(max_length=250)
    user_type = models.CharField(max_length=250, choices=UserTypes.choices)
    email     = models.EmailField(max_length=250)
    id        = models.AutoField(primary_key=True)