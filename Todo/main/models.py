from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Id will created automatic from django

class Todo(models.Model):
    
    importance_of_todo = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    
    title = models.CharField(max_length=50, null = True, blank = True)
    importance = models.CharField(max_length=6, null = True, blank = True, choices=importance_of_todo, default="High")
    email = models.EmailField(null = True, blank = True)
    is_done = models.BooleanField(null = True, default=False)
    created_date = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    
    def __str__(self):
        return self.title
    
    def getDescription(self):
        return self.description[:5] + "...."
    
class TodoItems(models.Model):
    task = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, auto_now_add = True, null = True)
    is_completed = models.BooleanField(null = True, default=False)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True, blank=True) 
    
    def __str__(self):
        return self.task
    
    
    
    
    
    
# one2one relationship ---> (relation_Schema_Name, on_delete=models.CASCADE or DO_NOTHING or SET_NULL ...) {from models file}
# many2many relationship ---> create the third schema autogenerate from django (by default) ----> put in anyone of them models.manytomany(schema_Name)
# many2one relationship ---> (models.ForeignKey( schema_Name, on_delete=models.CASCADE or DO_NOTHING or SET_NULL ...)){from models file}
# models.CASCADE ---> to remove parent entity
# models.SET_NULL ---> to put null in parent entity