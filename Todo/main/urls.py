from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detailed/<str:id>', views.detailed, name="detailed"),
    path('createTodo/', views.createTodo, name="createTodo"),
    path('updateTodo/<str:pk>', views.updateTodo, name="updateTodo"),
    path('deleteTodo/<str:pk>', views.deleteTodo, name="deleteTodo"),  
    path('register/', views.createUser, name="register"),
    path('createTodoItem/<str:pk>', views.createTodoItem, name="createTodoItem"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
