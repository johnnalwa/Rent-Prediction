from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)  # Assuming maximum phone length is 15 characters
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)  # You might want to hash passwords for security

    def __str__(self):
        return self.username
