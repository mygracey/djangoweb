from django.db import models

class  UserModel(models.Model):
    username=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.username
