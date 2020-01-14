from django.contrib import admin
from myblog.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    max_num = Category.objects.count() or 0
    extra = Category.objects.count() or 0
    
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    list_display = ['title', 'text', 'author', 'published_date']

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']
    list_display = ['name', 'description']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
