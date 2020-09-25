from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Modal(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True)
    modal_boolean = models.BooleanField(default=False)
    modal = models.ManyToManyField(Modal, blank=True)
    
    def __str__(self):
        return self.title


class DropDown(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=200, blank=True)
    item = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.title


class Attribute(models.Model):
    title = models.CharField(max_length=200)
    dropdown = models.ManyToManyField(DropDown, blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=200)
    attribute = models.ManyToManyField(Attribute, blank=True)

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    section = models.ManyToManyField(Section, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
