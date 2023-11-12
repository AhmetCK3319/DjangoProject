from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

     # slug alanının otomatik olarak dolmasını sağlar
    prepopulated_fields={'slug':('category_name',)}

    # her zamanki iş
    list_display=('category_name','slug','image_tag',)
