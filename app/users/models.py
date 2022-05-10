from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    rfc = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name