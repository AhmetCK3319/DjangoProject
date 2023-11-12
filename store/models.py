from django.db import models
from category.models import Category
from accounts.models import Account
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.db.models import Avg,Count


class Product(models.Model):
    product_name    = models.CharField(max_length=200,unique=True)
    slug            = models.SlugField(max_length=200,unique=True)
    description     = models.TextField(max_length=255)
    image           = models.ImageField(upload_to='photos/products')
    new_price       = models.IntegerField()
    old_price       = models.IntegerField()
    stock           = models.IntegerField()
    is_avaible      = models.BooleanField()
    category        = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])
    
    
    def average_review(self):
    # Check if there are any reviews for the product
        reviews = ReviewRating.objects.filter(product=self).aggregate(average=Avg('rating'))
        if reviews['average'] is not None:
            avg = float(reviews['average'])
            return avg
        else:
            # Handle the case where there are no reviews
            return 0  # You can return 0 or any other default value as needed
    
    
    def count_review(self):
        reviews = ReviewRating.objects.filter(product=self).aggregate(count=Count('id'))
        if reviews['count'] is not None:
            count = int(reviews['count'])
            return count
        else:
            # Handle the case where there are no reviews
            return 0  # You can return 0 or any other default value as needed


    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""
    image_tag.short_description = 'Image'



class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color',is_active=True)
    def sizes(self):
        return super(VariationManager,self).filter(variation_category='size',is_active=True)

variation_category_choice = (
('color','color'),
('size','size'),
)

class Variation(models.Model):
    product            = models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100,choices=variation_category_choice)
    variation_value    = models.CharField(max_length=100)
    is_active          = models.BooleanField(default=True)
    created_at         = models.DateTimeField(auto_now_add=True)

    objects=VariationManager()

    def __str__(self):
        return self.variation_value
    
class ReviewRating(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(Account,on_delete=models.CASCADE) 
    subject=models.CharField(max_length=100,blank=True)
    review=models.TextField(max_length=500,blank=True)
    rating=models.FloatField()
    ip=models.CharField(max_length=20,blank=True)
    status=models.CharField(max_length=20,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class  Meta:
        verbose_name='reviewrating'
        verbose_name_plural='Review rating'

    def __str__(self):
        return self.subject
    

class ProductGalery(models.Model):
    product=models.ForeignKey(Product,default=None,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='store/products',max_length=255)

    class  Meta:
        verbose_name='productgalery'
        verbose_name_plural='Product galery'



    def __str__(self):
        return self.product.product_name