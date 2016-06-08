""" This POC imports an excel spreadsheet into pinpoints vendor calculation
software.  This allows non-technical users to feed data into the application.

TODO: Build web interface for importing new information
"""
import sys, os
import pandas as pd

# Setup DJango
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pinpoint_vms.settings")
import django
django.setup()

# Import Models
from vendor_calculator.models import Vendor, Product, Configuration, VendorConfigurationProcess

def say(*args):
    """ This prints a line with a few stars prepended. It helps identify log
    message if the application is verbose

    TODO: Move to a central import thats executed during every python program
    """
    print("***",*(args))

def add_vendors(vendors):
    """ This creates Django models for various vendors.  If a vendor already
    exists, it is ignored
    """
    say('Attempting to add the vendors ', vendors)

    for vendor in vendors:
        # Skip Vendor if it already exists
        if(Vendor.objects.filter(company_name = vendor)):
            say('Vendor',vendor,'already exists')
            continue

        vendorModel = Vendor(company_name = vendor)
        vendorModel.save()
        say('Added vendor', vendor)

    print()

def add_products(products):
    say('Attempting to add the products', products)
    for product in products:
        # Skip Vendor if it already exists
        if(Product.objects.filter(product_name = product)):
            say('prodcut',product,'already exists')
            continue

        productModel = Product(product_name = product)
        productModel.save()
        say('Added product', product)

    print()

def add_configs(item,configs):
    # TODO IMPLEMENT THIS
    say('Attempting to add the configurations\n', item, ':', configs)
    say('***********************')
    say('IMPLEMENT ADDING CONFIGURATION TO DJANGO')
    say('***********************')
    print()

if(__name__=='__main__'):
    # Load excel document
    fname = os.path.abspath(sys.argv[1])
    say("Importing Excel Document ", fname)
    df = pd.read_excel(fname)
    say("First 5 rows look like\n", df.head())

    # Clean the data
    say("Replacing 'n/a' and NaN with null values")
    df = df.fillna('n/a').replace({'n/a':None})
    say("Cleaned first 5 rows look like\n", df.head())

    # Add Vendors contained in the header
    header = [colHeader.title() for colHeader in df.columns.values]
    say("Dataframe header is ",header)
    # Expect first to columns to not be vendor names
    non_vendor_columns = ['Item', 'Configuration']
    actual_non_vendor_columns = header[:2]
    vendor_columns = header[2:]
    if(actual_non_vendor_columns != non_vendor_columns):
        say('First two columns must be ', non_vendor_columns, ', but they are ',
              non_vendor_columns, '. \nEXITING')
        exit(1)
    add_vendors(vendor_columns)

    # Get Products
    item_column = df.columns.values[0]
    products = pd.unique(df[item_column])
    add_products(products)

    # Get Configurations
    config_column = df.columns.values[1]
    item_config_group = df[[item_column,
                       config_column]].groupby(item_column)
    item_configs = {k:list(v) for k,v in item_config_group[config_column]}
    for item, configs in item_configs.items():
        add_configs(item, configs)

    # TODO Get configuration cost per venor
