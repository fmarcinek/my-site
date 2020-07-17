from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.storage import default_storage as storage
from django_resized import ResizedImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ResizedImageField(size=(300, 300), quality=100, default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     if self.image and 'profile_pics' not in self.image.name:
    #         img = Image.open(self.image)
    #         if img.height > 300 or img.width > 300:
    #             output_size = (300, 300)
    #             img.thumbnail(output_size)
    #             output = BytesIO()
    #             img.save(output, format='png')
    #             output.seek(0)
    #             self.image = InMemoryUploadedFile(output, 'ImageField', self.image.name, 'image/png',
    #                                               sys.getsizeof(output.getbuffer()), None)
    #     super().save(*args, **kwargs)

