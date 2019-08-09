from django.db import models

# Create your models here.
class Support(models.Model):
    support = models.CharField(max_length=128)

    def __str__(self):
        return self.support
