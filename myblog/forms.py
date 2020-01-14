from django.forms import ModelForm, DateTimeInput
from myblog.models import Post, Category

class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'text', 'author', 'published_date', 'new_field']
        exclude = ['created_date', 'modified_date']
        widgets = {
            'published_date': DateTimeInput(attrs={'type': 'date'})
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        