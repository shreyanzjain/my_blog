from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile-pics')

    def __str__(self):
        return f'@{self.user.username} profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            op_size = (300, 300)
            img.thumbnail(op_size)
            width, height = img.size
            left = (width - 300)/2
            right = (width + 300)/2
            top = (height - 300)/2
            bottom = (height + 300)/2
            img = img.crop((left, top, right, bottom))
            img.save(self.image.path)