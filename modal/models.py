from django.db import models

# Create your models here.
class ModalData(models.Model):
    title = models.CharField(max_length=200)
    data_style = models.CharField(max_length=200)
    data = models.CharField(max_length=500)

    @classmethod
    def add_modal_data(cls, request, form, section):
        add_data_form = form(request.POST)
        if add_data_form.is_valid():
            data = add_data_form.save(commit=False)
            data.save()
            section.modal_data.add(data)

    def __str__(self):
        return self.title


class ModalSection(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=250, blank=True)
    modal_data = models.ManyToManyField(ModalData, blank=True)

    def __str__(self):
        return self.title
