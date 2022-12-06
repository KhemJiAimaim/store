from django.contrib import admin
from .models import User , Products , Category ,  Payment , Debtors
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['barcode' , 'name' , 'price' , 'category' , 'show_image']
    search_fields = ['barcode' , 'name']

    fieldsets = (
        (None, {'fields': ['barcode' , 'name' , 'price' , 'cost', 'image'] }),
        ('Category' , {'fields': ['category'] , 'classes' : ['collapse']}),
    )


admin.site.register(User)
admin.site.register(Products,ProductAdmin)
admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(Debtors)
