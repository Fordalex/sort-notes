from django.db import models

# Create your models here.
class ModalData(models.Model):
    title = models.CharField(max_length=200)
    data = models.JSONField(encoder=None, decoder=None)
    data_style = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class ModalSection(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=250, blank=True)
    modal_data = models.ManyToManyField(ModalData, blank=True)

    def __str__(self):
        return self.title

class Modal(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=250, blank=True)
    modal_section = models.ManyToManyField(ModalSection, blank=True)

    def __str__(self):
        return self.title
