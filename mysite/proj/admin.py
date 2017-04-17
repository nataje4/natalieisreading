from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(Blurb)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Post)



''' class BookAdmin(admin.ModelAdmin):

class AuthorAdmin(admin.ModelAdmin): '''
