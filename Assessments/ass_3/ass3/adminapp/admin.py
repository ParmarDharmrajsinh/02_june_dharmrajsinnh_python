from django.contrib import admin
from .models import User, Category, Post, Comment

# Customize User Admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'caption', 'image')
    list_filter = ('author',)
    search_fields = ('caption',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'text')
    search_fields = ('text',)


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_header = "Blog Admin Panel"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Manage Blog Application"
