from django.contrib import admin

from .models import Vendor, Product, Configuration
from .models import VendorConfigurationProcess

admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Configuration)
admin.site.register(VendorConfigurationProcess)
