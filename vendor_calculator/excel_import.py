import sys
from os.path import abspath
import pandas as pd

#from models import Vendor, Product, Configuration, VendorConfigurationProcess

def say(*args):
    print("***",*(args))

def add_vendors(vendors):
    say('Attempting to add the vendors ', vendors)
    say('***********************')
    say('IMPLEMENT ADDING VENDORS TO DJANGO')
    say('***********************')
    print()

def add_products(products):
    say('Attempting to add the products', products)
    say('***********************')
    say('IMPLEMENT ADDING PRODUCTS TO DJANGO')
    say('***********************')
    print()

def add_configs(item,configs):
    say('Attempting to add the configurations', item, ':', configs)
    say('***********************')
    say('IMPLEMENT ADDING CONFIGURATION TO DJANGO')
    say('***********************')
    print()

if(__name__=='__main__'):
    # Load excel document
    fname = abspath(sys.argv[1])
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
    item_configs = df[[item_column, config_column]].groupby(item_column)
    for item, configs in item_configs:
        add_configs(item, configs)
