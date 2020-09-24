from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('subject/<pk>', views.subject, name="subject"),
    # add urls
    path('add_subject/', views.add_subject, name="add_subject"),
    path('add_section/<pk>', views.add_section, name="add_section"),
    path('add_attribute/<pk>/<subject_pk>', views.add_attribute, name="add_attribute"),
    path('add_dropdown/<attribute_pk>/<subject_pk>', views.add_dropdown, name="add_dropdown"),
    path('add_item/<pk>/<subject_pk>', views.add_item, name="add_item"),
    # edit urls
    path('edit_subject/<subject_pk>', views.edit_subject, name="edit_subject"),

    # remove data
    path('remove_data/<data_type>/<pk>', views.remove_data, name="remove_data"),
]
