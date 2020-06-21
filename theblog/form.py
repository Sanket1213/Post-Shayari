from django import forms
from .models import Post, Category

# choices=[('coding','coding'),('sports','sports'),('birthday','birthday'),]

choices=Category.objects.all().values_list('name', 'name')
choice_list=[]
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'category', 'shayari')

        widgets = {
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'category' : forms.Select(choices=choice_list, attrs={'class': 'form-control', 'value':'shayari'}),
            'shayari' : forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'shayari')

        widgets = {
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'shayari' : forms.Textarea(attrs={'class': 'form-control'}),

        }

class WalgarPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'category', 'shayari')

        widgets = {
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'category' : forms.TextInput(attrs={'class': 'form-control', 'value':'walgar', 'type':'hidden'}),
            'shayari' : forms.Textarea(attrs={'class': 'form-control'}),
        }
