from constants.django import models    
from constants.random import uuid

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True,default=uuid.uuid4)
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)
    auth_token = models.CharField(max_length=255,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']
        unique_together = ('email', 'phone')

