from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from users.models import Cart
from orders.models import Item
from shopping_cart.extras import generate_order_id, transact, generate_client_token
from shopping_cart.models import OrderItem, Order, Transaction


# Create your views here.

def get_user_pending_order(request):
    # get order for the correct user
    user_cart = get_object_or_404(Cart, user=request.user)
    order = Order.objects.filter(owner=user_cart, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required()
def add_to_cart(request, **kwargs):
    # get the user cart
    user_cart = get_object_or_404(Cart, user=request.user)
    # filter items by id
    item = Item.objects.filter(id=kwargs.get('item_id', "")).first()

    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(item=item)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_cart, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('orders:orders-home'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)


@login_required()
def checkout(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/checkout.html', context)

