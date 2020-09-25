from django.db import models

# Create your models here.
class Modal(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=250)

    def __str__(self):
        return self.title
