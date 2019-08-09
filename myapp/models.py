from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField('date published')
    state = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    feature = models.TextField()
    user = models.CharField(max_length=30)

    def __self__(self):
        return self.name