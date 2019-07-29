from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField('date published')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __self__(self):
        return self.name