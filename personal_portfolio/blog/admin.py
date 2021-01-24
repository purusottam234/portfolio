from django.contrib import admin

# Register your models here.
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post)
admin.site.register(Category)
