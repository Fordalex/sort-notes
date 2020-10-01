from django.db import models

# Create your models here.
class ModalData(models.Model):
    title = models.CharField(max_length=200)
    data_style = models.CharField(max_length=200)
    data = models.CharField(max_length=500)
    image = models.ImageField(null=True, blank=True)

    @classmethod
    def add_modal_data(cls, request, section, data):
        data_object = cls(
            title = request.POST.get('title'),
            data_style = request.POST.get('data_style'),
            data = data,
        )
        data_object.save()
        section.modal_data.add(data_object)

    def __str__(self):
        return self.title


class ModalSection(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=250, blank=True)
    modal_data = models.ManyToManyField(ModalData, blank=True)

    def __str__(self):
        return self.title
