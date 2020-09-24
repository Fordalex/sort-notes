from django.contrib import admin
from .models import Subject, Section, Attribute, DropDown, Item


# Register your models here.
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Attribute)
admin.site.register(DropDown)
admin.site.register(Item)