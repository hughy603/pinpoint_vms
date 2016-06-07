from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse
from django import forms

from .models import Vendor, Product, Configuration
from .models import VendorConfigurationProcess

def index(request):
    return render(request, 'vendor_calculator/index.html')

class SearchForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all().order_by('product_name'),
        widget=forms.Select(attrs={"onChange":'submit()'}),
    )
    maximum_arrival_days = forms.IntegerField(
        min_value = 1,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            product_id = ''
        else:
            product_id = args[0].get('product', '')
        super(SearchForm, self).__init__(*args, **kwargs)
        if product_id != '':
            product = Product.objects.get(pk=product_id)
            self.fields['configuration'] = forms.ModelChoiceField(
                queryset = product.configuration_set.all().order_by('name')
            )

class SearchView(generic.FormView):
    form_class = SearchForm
    template_name = 'vendor_calculator/search.html'

    def get(self, request, *arg, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            configuration = form.cleaned_data['configuration']
            configs = configuration.vendorconfigurationprocess_set
            if form.cleaned_data['maximum_arrival_days']:
                configs = configs.filter(
                    max_processing_days__lte=form.cleaned_data['maximum_arrival_days'],
                )
            configs = configs.order_by('cost')
            return render(request, 'vendor_calculator/search_results.html',
                          {'config_list':configs})
        return render(request, self.template_name, {'form': form})


class VendorView(generic.ListView):
    template_name = 'vendor_calculator/vendors.html'
    context_object_name = 'vendor_list'

    def get_queryset(self,):
        return Vendor.objects.order_by('company_name')

class VendorDetailView(generic.ListView):
    model = Vendor
    template_name = 'vendor_calculator/vendor.html'
