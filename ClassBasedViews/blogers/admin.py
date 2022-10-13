from django.contrib import admin

from .models import AuthorModel, BlogModel, EntryModel

# Register your models here.

admin.site.register(AuthorModel)
admin.site.register(BlogModel)
admin.site.register(EntryModel)

