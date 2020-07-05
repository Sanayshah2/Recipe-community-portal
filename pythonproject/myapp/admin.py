from django.contrib import admin

# Register your models here.
from .models import Food
from .models import Category
from .models import Comment


admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Comment)

