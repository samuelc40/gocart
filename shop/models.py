from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    img = models.ImageField(upload_to='categories')

    class Meta:
        ordering = ('name',)
        verbose_name = 'categories'
        verbose_name_plural = 'categ'

    def get_url(self):
        return reverse('prod_cat', args=[self.slug])

    
    def __str__(self):
        return '{}'.format(self.name)

class products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.CharField(max_length=150, unique=True)
    img = models.ImageField(upload_to='products')
    img1 = models.ImageField(upload_to='products')
    img2 = models.ImageField(upload_to='products')
    img3 = models.ImageField(upload_to='products')
    imgin = models.ImageField(upload_to='products')
    desc = models.TextField()
    desc1 = models.TextField()
    stock = models.IntegerField()
    old_price = models.IntegerField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    showsize = models.BooleanField(default=True)
    categories = models.ForeignKey(category, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details', args=[self.categories.slug, self.slug])
    
    def __str__(self):
        return '{}'.format(self.name)




