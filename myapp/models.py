from django.db import models

# Create your models here.


class Article(models.Model):
    date = models.DateField(auto_now_add=True)
    print(date)
    heading = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="article_images")


