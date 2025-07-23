from django.contrib import admin

# Register your models here.

from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("author", "date", )
    list_display = ("title", "author", )
    
admin.site.register(Post, PostAdmin)
admin.site.register(Author)    
admin.site.register(Tag)