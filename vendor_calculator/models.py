from django.db import models

# Create your models here.
class Vendor(models.Model):
    company_name = models.CharField(max_length=200, unique = True)
    website = models.CharField(max_length=200, blank = True)
    turnaround_time = models.CharField(max_length=200, blank = True)
    mistakes = models.CharField(max_length=200, blank = True)
    product_options = models.CharField(max_length=200, blank = True)
    customer_service = models.CharField(max_length=200, blank = True)
    where_to_place_order = models.CharField(max_length=200, blank = True)
    contact = models.CharField(max_length=200, blank = True)
    address = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return self.company_name

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique = True)
    description =  models.CharField(max_length=4000)

    def __str__(self):
        return self.product_name

class Configuration(models.Model):
    product = models.ForeignKey(Product,
                                on_delete  = models.CASCADE)
    description =  models.CharField(max_length=1000,unique = True)

    def __str__(self):
        return "{0} with {1}({2})" \
                .format(self.product,
                       self.name,
                       self.description,
                       )

class VendorConfigurationProcess(models.Model):
    vendor = models.ForeignKey(Vendor,
                               on_delete = models.CASCADE)
    configuration = models.ForeignKey(Configuration,
                               on_delete = models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    min_processing_days = models.PositiveIntegerField(default=1)
    max_processing_days = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{} offers the product {} for ${}. It will arrive in " \
                "{} to {} days".format(self.vendor,
                                       self.configuration,
                                       self.cost,
                                       self.min_processing_days,
                                       self.max_processing_days,
                                      )

