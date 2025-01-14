from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics', default='default.jpg')
    address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
    
    def __str__(self):
        return f'{self.user.username} Profile'