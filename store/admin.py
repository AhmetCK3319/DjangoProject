from django.contrib import admin
from .models import Product,Variation,ReviewRating,ProductGalery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGaleryInline(admin.TabularInline):

    model=ProductGalery

    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display=('product_name','slug','new_price','old_price','category','is_avaible','image_tag')

    prepopulated_fields={'slug':('product_name',)}

    inlines=[ProductGaleryInline]



@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):

    list_display  = ('product','variation_category','variation_value','is_active')

    list_editable = ('is_active',)

    list_filter = ('product','variation_category','variation_value')



@admin.register(ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):

    list_display  = ('product','user','rating','ip','created_date')

    list_filter = ('review','rating')



admin.site.register(ProductGalery)

