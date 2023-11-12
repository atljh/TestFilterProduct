from django.db import models

class FilterNumbers(models.Model):
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Filter Number"
        verbose_name_plural = "Filter Numbers"

class Product(models.Model):
    name = models.CharField(max_length=255)
    productCode = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.URLField()
    currency = models.CharField(max_length=3)
    qty = models.IntegerField()
    filter_numbers = models.ManyToManyField(FilterNumbers)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
