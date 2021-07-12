from django.db import models

# Create your models here.


class AffiliateModel(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/affliate_img',
                            width_field='img_width', height_field='img_height')
    img_width = models.IntegerField(default=600)
    img_height = models.IntegerField(default=350)
    desc = models.TextField()
    url_img = models.URLField()

    def __str__(self):
        return self.title
