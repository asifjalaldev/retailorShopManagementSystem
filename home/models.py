from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    costprice=models.IntegerField()
    saleprice=models.IntegerField()
    qty=models.IntegerField(default=1)
    prod_model=models.CharField(max_length=50, null=True)
    profit=models.IntegerField(default=0)
    countsoldProduct=models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Sold_prduct(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    qty=models.IntegerField()
    date=models.DateField()
    costprice=models.IntegerField()
    discount=models.IntegerField(default=0)
    profit=models.IntegerField(default=0)
    def __str__(self):
        return self.product.name
# class Jazzcash_in(models.Model):
#     jazzcash_balance_in= models.DecimalField(max_digits=10, decimal_places=2)
#     date=models.DateField()
#     def __str__(self):
#         return self.jazzcash_balance_in
# class Jazzcash_out(models.Model):
#     jazzcash_balance_out= models.DecimalField(max_digits=10, decimal_places=2)
#     date=models.DateField()
#     def __str__(self):
#         return self.jazzcash_balance_out
# class Easypaisa_in(models.Model):
#     easypaisa_balance_in= models.DecimalField(max_digits=10, decimal_places=2)
#     date=models.DateField()
#     def __str__(self):
#         return self.easypaisa_balance_in
# class Easypaisa_out(models.Model):
#     easypaisa_balance_out= models.DecimalField(max_digits=10, decimal_places=2)
#     date=models.DateField()
#     def __str__(self):
#         return self.easypaisa_balance_out