from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    State_origin = models.CharField( default='State of Origin', max_length=100)
    permanent_address = models.TextField(default='')
    residential_address = models.TextField(default='')


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img= Image.open(self.image.path)
        output_size = (300,300)

        if img.width > 400 or img.height > 400:
            img.thumbnail(output_size)
            img.save(self.image.path)

