from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    country = models.CharField(default='', max_length=50)
    city = models.CharField(default='', max_length=50)
    facebook_page = models.CharField(max_length=255, null=True, blank=True)
    instagram_page = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('contact-user', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


