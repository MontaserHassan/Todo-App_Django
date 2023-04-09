from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detailed/<str:id>', views.detailed, name="detailed"),
    path('createTodo/', views.createTodo, name="createTodo"),
    path('updateTodo/<str:pk>', views.updateTodo, name="updateTodo"),
    path('deleteTodo/<str:pk>', views.deleteTodo, name="deleteTodo"),    
]
