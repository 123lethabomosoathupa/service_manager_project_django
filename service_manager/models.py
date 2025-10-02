from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
        default='https://res.cloudinary.com/demo/image/upload/v1690000000/placeholder.png'
    )

    def __str__(self):
        return self.title
