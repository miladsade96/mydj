from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'created_date', 'published_date')
    list_filter = ('author', 'status', 'created_date', 'published_date')
    search_fields = ('title', 'content')
    summernote_fields = ('content',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
