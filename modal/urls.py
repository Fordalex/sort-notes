from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<subject_pk>/<item_pk>', views.modal, name="modal"),
    # add urls
    path('add_information/<subject_pk>/<item_pk>', views.add_information, name="add_information")
]
