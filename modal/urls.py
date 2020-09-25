from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<subject_pk>/<item_pk>', views.modal, name="subject"),
    # add urls

]
