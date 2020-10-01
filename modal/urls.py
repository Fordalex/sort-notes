from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<subject_pk>/<item_pk>', views.modal, name="modal"),
    # add urls
    path('edit_modal_section/<subject_pk>/<item_pk>/<section_pk>', views.edit_modal_section, name="edit_modal_section"),
    path('edit_data/<modal_data_pk>/<section_pk>/<item_pk>/<subject_pk>', views.edit_data, name="edit_data"),
    # remove urls
    path('remove_data/<data_type>/<data_pk>/<subject_pk>/<item_pk>', views.remove_data, name="remove_data"),
]
