from unicodedata import name
from django.urls import path

from .views import (
    dashboard,
    storeNote,
    detail,
    storeItem,
    storeObservation,
    updateNote,
    updateItem,
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('addNotes/', storeNote, name='note.add'),
    path('updateNote/<int:id>/', updateNote, name='note.update'),
    path('detailNote/<int:id>/', detail, name='note.detail'),
    path('addItem/<int:id>', storeItem, name='item.add'),
    path('updateItem/<int:id>', updateItem, name='item.update'),
    path('addObservation/<int:id>', storeObservation, name='observation.add'),
]