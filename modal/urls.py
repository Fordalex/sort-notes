from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<subject_pk>/<item_pk>', views.modal, name="modal"),
    # add urls
    path('add_modal_section/<subject_pk>/<item_pk>', views.add_modal_section, name="add_modal_section"),
    path('add_data/<section_pk>/<item_pk>', views.add_data, name="add_data"),
    # Edit urls
    path('edit_modal_section/<item_pk>', views.edit_modal_section, name="edit_modal_section")
]
