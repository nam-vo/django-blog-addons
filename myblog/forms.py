from django.forms import ModelForm, ModelMultipleChoiceField
from myblog.models import Post, Category

class PostForm(ModelForm):
    new_field = ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'published_date', 'new_field']
        # exclude = ['created_date', 'modified_date']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        