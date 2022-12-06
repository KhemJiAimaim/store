from django.db import models
from django.utils.html import format_html


# Create your models here.

#ผู้ใช้
class User(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    tel = models.IntegerField()

    def __str__(self) :
        return self.username
    
    class Meta:
        verbose_name_plural = 'User'

#หมวดหมู่
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name_plural = 'Category'

#สินค้า
class Products (models.Model):
    name = models.CharField(max_length=250 , unique=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    cost = models.IntegerField()
    category = models.ForeignKey(Category, null=True , blank=True , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload'  , blank=True , unique=True)
    barcode = models.CharField(max_length=250 , unique=True)

    class Meta:
        ordering = ['quantity'] #เรียงจากน้อยไปมาก ถ้า -quantity จะเป็นจากมากไปน้อย
        verbose_name_plural = 'Products'
    
    def __str__(self) :
        return self.name
    
    def show_image(self):
        if self.image:
            return format_html('<img src= '+self.image.url+' height= "80px" >' )
            return ''
        show_image.allow_tags = True
                

        #ชำระเงิน
class Payment(models.Model):
    product = models.ManyToManyField(Products, blank=True)
    price = models.FloatField(default=0)
    DateTime = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Payment'

#ลูกหนี้
class Debtors (models.Model):
    payment = models.ManyToManyField(Payment, blank=True)
    name = models.CharField(max_length=250)
    tel = models.IntegerField()
    price = models.FloatField(default=0)
    debtDateTime = models.DateTimeField(auto_now_add=True) # วันที่ติดหนี้
    updateDateTime= models.DateTimeField(auto_now=True) #วันที่จ่ายหนี้

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name_plural = 'Debtors'


    
    
