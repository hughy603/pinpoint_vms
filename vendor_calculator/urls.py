from django.conf.urls import url

from . import views

app_name = 'vendor_calculator'
urlpatterns = [
    # ex /vendor_calculator/
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^vendors/$', views.VendorView.as_view(), name='vendors'),
    url(r'^vendors/(?P<pk>[0-9]+)/$', views.VendorDetailView.as_view(), name='vendor_detail'),
]
