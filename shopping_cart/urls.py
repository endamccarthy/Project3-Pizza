from django.conf.urls import url
from django.urls import path

from .views import (add_to_cart, delete_from_cart, order_details, checkout, success, update_transaction_records, clear_cart)

app_name = 'shopping_cart'

urlpatterns = [
    path('add-to-cart/', add_to_cart, name="add_to_cart"),
    path('order-summary/', order_details, name="order_summary"),
    #url(r'^add-to-cart/$', add_to_cart, name="add_to_cart"),
    #url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^success/$', success, name='purchase_success'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^update-transaction/$', update_transaction_records, name='update_records'),
    url(r'^clear-cart/$', clear_cart, name='clear_cart')
]