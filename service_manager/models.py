from django.db import models

class Service(models.Model):
    # Title of the service
    title = models.CharField(max_length=100, default="Untitled Service")
    # Description of the service
    description = models.TextField()

    # Image upload field - linked to Cloudinary storage
    # A default placeholder will be used if no image is uploaded
    image = models.ImageField(
        upload_to='services/',
        blank=True,
        null=True,
        default='https://res.cloudinary.com/demo/image/upload/v1690000000/placeholder.png'  # 👈 placeholder image URL
    )

    def __str__(self):
        return self.title