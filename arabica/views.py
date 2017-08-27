from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
import json
from decimal import Decimal



def ajaxcalculation(request):
	total = Decimal(0)

	bean_id = request.GET.get('bean')
	if bean_id:
		total += CoffeeBean.objects.get(id=bean_id).price

	roast_id = request.GET.get('roast')
	if roast_id:
		total += Roast.objects.get(id=roast_id).price

	shots = request.GET.get('shots')
	total += Decimal(int(shots) * 0.500)

	milk = request.GET.get('milk')
	if milk:
		total += Decimal(0.250)

#json.loads de-stringifies the JSON.stringify in the script that was used for the list IDs
	syrups = json.loads(request.GET.get('syrups'))
	for syrup in syrups:
		total += Syrup.objects.get(id=syrup).price
	
	powders = json.loads(request.GET.get('powders'))
	for powder in powders:
		total += Powder.objects.get(id=powder).price

	print(round(total, 3))
	return JsonResponse(total, safe=False)

def address(request):
	if not (request.user.is_authenticated):
		raise Http404()
	form = AddressForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Address has been added.")
		return redirect("arabica:list")
	context = {
	"form": form,
	}
	return render(request, 'address.html', context)

def adminlist(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404()
	users = User.objects.all()
	context = {
	"users": users,
	}
	return render(request, 'adminlist.html', context)

def update(request, order_id):
	order = get_object_or_404(Coffee, id= order_id)
	if not (request.user.is_staff or request.user.is_superuser or order.user == request.user):
		raise Http404()
	form = OrderForm(request.POST or None, instance = order)
	if form.is_valid():
		form.save()
		messages.success(request, "Your order has been updated.")
		return redirect(order.absurl())
	context = {
	"form": form,
	"order": order,
	}
	return render(request, 'update.html', context)


def orderdetail(request, order_id):
	obj = get_object_or_404(Coffee, id=order_id)
	if not (request.user.is_staff or request.user.is_superuser or obj.user == request.user):
		raise Http404()
	context = {
	"x": obj,
	}
	return render(request, 'detail.html', context) 

def delete(request, order_id):
	if not (request.user.is_staff or request.user.is_superuser or obj.user == request.user):
		raise Http404()
	order = get_object_or_404(Coffee, id= order_id)
	order.delete()
	messages.success(request, "Order deleted.")
	return redirect("arabica:list")

def orderlist(request):
	order_list = request.user.coffee_set.all().order_by("-completed") 

	query = request.GET.get("q")
	if query:
		order_list = order_list.filter(
			Q(name__icontains=query)
			).distinct()

	context = {
	"order_list": order_list,
	"user": request.user,
	}
	return render(request, 'list.html', context) 

def rbsp(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404()
	
	roast_form = RoastForm(request.POST or None)
	if roast_form.is_valid():
		roast_form.save()
		messages.success(request, "Thank you for adding a roast.")
		return redirect("arabica:rbsp")
	
	bean_form = CoffeeBeanForm(request.POST or None)
	if bean_form.is_valid():
		bean_form.save()
		messages.success(request, "Thank you for adding a bean.")
		return redirect("arabica:rbsp")	

	syrup_form = SyrupForm(request.POST or None)
	if syrup_form.is_valid():
		syrup_form.save()
		messages.success(request, "Thank you for adding a syrup.")
		return redirect("arabica:rbsp")

	powder_form = PowderForm(request.POST or None)
	if powder_form.is_valid():
		powder_form.save()
		messages.success(request, "Thank you for adding a powder.")
		return redirect("arabica:rbsp")


	context = {
	"roast_form": roast_form,
	"bean_form": bean_form,
	"syrup_form": syrup_form,
	"powder_form": powder_form,
	}
	
	return render(request, 'rbsp.html', context)

def order(request):
	if not (request.user.is_authenticated):
		raise Http404()
	order_form = OrderForm(request.POST or None)
	if order_form.is_valid():
		# obj = order_form.save(commit=False)
		obj = order_form.save()
		obj.price = obj.coffeeprice()
		obj.user = request.user
		obj.save()
		messages.success(request, "Thank you for your order.")
		return redirect("arabica:list")
	context = {
	"order_form": order_form,
	}
	return render(request, 'order.html', context)

def usersignup(request):
	context = {}
	form = UserSignUp()
	context['form'] = form
	if request.method == "POST":
		form = UserSignUp(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = user.username
			password = user.password
			email = user.email
			first_name = user.first_name
			last_name = user.last_name
			user.set_password(password)
			user.save()
			auth_user = authenticate(username=username, password=password)
			login(request, auth_user)
			return redirect("arabica:home")
		else:
			messages.error(request, form.errors)
			return redirect("arabica:signup")

	return render(request, 'signup.html', context)

def userlogout(request):
	logout(request)
	return redirect("arabica:home")

def userlogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form
	if request.method == 'POST':
		form = UserLogin(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect('arabica:home')

			messages.error(request, "Wrong username/password combination. Please try again.")
			return redirect("arabica:login")
		messages.error(request, form.errors)
		return redirect("arabica:login")
	return render(request, 'login.html', context)

def home(request):
	return render(request, 'home.html', {})