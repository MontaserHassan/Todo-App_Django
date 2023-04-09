from django.forms import ModelForm, TextInput
from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        widget = {
            "title": TextInput(attrs={
                "color": "blue",
                "class": "form-control"
            }),
            "email": TextInput(attrs={
                "color": "blue",
                "class": "form-control"
            }),
            # "importance": forms.Select(choices=Todo.importance_of_todo),
            # "is_done": forms.CheckboxInput(),
            # "created_date": forms.HiddenInput(),
        }