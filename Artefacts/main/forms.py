from django.forms import ModelForm, FileInput, Textarea
from .models import Products

class AddForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'image_source']

        widgets = {
            "name": Textarea(attrs={
                'class': 'name',
                'placeholder': 'Название',
                'cols': "32",
                'rows': "2",
                'style': "resize: none;"
            }),
            "description": Textarea(attrs={
                'class': 'descr',
                'placeholder': 'Описание',
                'cols': "32",
                'rows': "5",
                'style': "resize: none;"
            }),
            "price": Textarea(attrs={
                'class': 'price',
                'placeholder': 'Цена в 📀',
                'cols': "32",
                'rows': "1",
                'style': "resize: none;"
            }),
            "image_source": FileInput(attrs={
                'type': 'file',
                'class':"plus",
                'cols': "32",
                'rows': "1",
            })
        }