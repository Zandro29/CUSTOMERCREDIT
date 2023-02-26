from django.db import models
#addition
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return super(ProductManager, self).get_queryset().filter(is_active=True)

class Customer(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'customers'
    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])
    def __str__(self):
        return self.name

class Credit(models.Model):
    customer = models.ForeignKey(Customer, related_name='credit', on_delete=models.CASCADE) 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit_creator')
    description = models.TextField(blank=True)
    amount_credit = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'credits'
        ordering = ('-created',)
    
    def get_absolute_url(self):
        return reverse('credit:credit_detail', args=[str(self.id)])

    def __str__(self):
        return self.customer.name