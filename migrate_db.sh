#!/bin/bash
python manage.py makemigrations vendor_calculator
python manage.py makemigrations
python manage.py migrate
