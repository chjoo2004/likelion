
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name="board"),
    path('diary/', views.diary, name="diary"),
    path('<int:pk>', views.board_one, name="board_one"),
    path('update/<int:pk>', views.board_update, name="board_update"),
    path('delete/<int:pk>', views.board_delete, name="board_delete"),
]
