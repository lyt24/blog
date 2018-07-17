from django.contrib import admin
from .models import BlogType, Blog


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    # list_display 可以显示元祖和列表，本例最好用元组，因为不可变，元祖中只有一个元素时不要哇估计逗号
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'author', 'get_read_num', 'created_time', 'last_updated_time')
