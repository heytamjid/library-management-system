from django.contrib import admin
from .models import *


class BookAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('bookname',)}
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Review)
admin.site.register(Category)
