
from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200)  # Title as a character field (max length 200)
    image = models.ImageField(upload_to='home_images/')  # Image field to upload images, the directory will be 'home_images/'

    def __str__(self):
        return self.title







