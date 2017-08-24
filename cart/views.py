from django.shortcuts import render, redirect
from .models import Cart, CartItem, Order
from arabica.models import Coffee, Address
from django.http import Http404
from .forms import *

def mycart(request):
	cart, created = Cart.objects.get_or_create(user=request.user)

	item_id = request.GET.get("item")
	qty = request.GET.get("qty", 1)

	if item_id:
		coffee = Coffee.objects.get(id=item_id)
		cart_item, created = CartItem.objects.get_or_create(cart=cart, item=coffee)

		if int(qty) < 1:
			cart_item.delete()

		else:
			cart_item.quantity = int(qty)
			cart_item.save()

	return render(request, 'cart.html', {'cart': cart})

def create_address(request):
	form = AddressForm

	if request.method == 'POST':
		form = AddressForm(request.POST)
		if form.is_valid():
			address = form.save(commit=False)
			address.user = request.user
			address.save()
			form.save()
			return redirect("cart:select_address")

	context = {
	"form": form
	}
	return render(request, 'create_address.html', context)

def select_address(request):
	if Address.objects.filter(user=request.user).count() < 1:
		return redirect("cart:create_address")
	form = AddressSelectForm()
	if request.method == 'POST':
		form = AddressSelectForm(request.POST)
		if form.is_valid():
			selected_address = form.cleaned_data['address']
			order = Order.objects.get(request.user)
			order.address = selected_address
			order.save()
			return redirect("/") #redirect back to checkout

	context = {
		'form': form
	}
	return render (request, 'select_address.html', context)

