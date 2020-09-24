from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('subject/<pk>', views.subject, name="subject"),
    path('edit_subject/', views.edit_subject, name="edit_subject"),
    path('edit_section/<pk>', views.edit_section, name="edit_section"),
    path('edit_attribute/<pk>', views.edit_attribute, name="edit_attribute"),
    path('edit_dropdown/<pk>', views.edit_dropdown, name="edit_dropdown"),
    path('edit_item/<pk>', views.edit_item, name="edit_item"),
]
