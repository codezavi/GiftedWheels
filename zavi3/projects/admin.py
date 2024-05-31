from django.contrib import admin

# Register your models here.
from .models import Project
from .models import review
from .models import Tag

admin.site.register(Project)
admin.site.register(review)
admin.site.register(Tag)