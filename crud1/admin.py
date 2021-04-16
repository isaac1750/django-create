from django.contrib import admin
from crud1.models import Author

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name',)
    
admin.site.register(Author, AuthorAdmin)
