from django.contrib import admin

from .models import Customer, Credit
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['customer', 'amount_credit', 'created', 'updated' , 'is_active']
    list_filter = ['is_active']
    list_editable = ['amount_credit', 'is_active']