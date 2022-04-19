from django.urls import path

from .views import (
    display,
    store,
    detail,
    update,
    delete,
)

urlpatterns = [
    path('allusers/', display, name='list.users'),
    path('addUser/', store, name='add.user'),
    path('detailUser/<int:id>', detail, name='detail.user'),
    path('updateUser/<int:id>', update, name='update.user'),
    path('deleteUser/<int:id>', delete, name='user.delete'),
]