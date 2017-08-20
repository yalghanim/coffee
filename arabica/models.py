from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from decimal import Decimal

class Roast(models.Model):
	roast_type = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=4, decimal_places=3)

	def __str__(self):
		return self.roast_type

class Syrup(models.Model):
	syrup_type = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=4, decimal_places=3)

	def __str__(self):
		return self.syrup_type

class Powder(models.Model):
	powder_type = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=4, decimal_places=3)

	def __str__(self):
		return self.powder_type

class CoffeeBean(models.Model):
	bean_type = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=4, decimal_places=3)

	def __str__(self):
		return self.bean_type

class Coffee(models.Model):
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	shots_choices = (
    (ONE, 'One'),
    (TWO, 'Two'),
    (THREE, 'Three'),
    (FOUR, 'Four'),
    (FIVE, 'Five'),
	)
#in case it doesnt work, use positiveintegerfield

	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=50)
	bean_type = models.ForeignKey(CoffeeBean)
	roast_type = models.ForeignKey(Roast)
	shots_number = models.IntegerField(default=ONE, choices=shots_choices) 
	syrup_type = models.ManyToManyField(Syrup)
	powder_type = models.ManyToManyField(Powder)
	water = models.FloatField(blank=True, null=True, default='')
	milk = models.BooleanField(default=False)
	foam = models.FloatField(blank=True, null=True, default='')
	extra_instructions = models.TextField(blank=True, null=True, default='')
	price = models.DecimalField(max_digits=6, decimal_places=3, default=0)
	completed = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
	
	def absurl(self):
		return reverse("arabica:detail", kwargs={"order_id": self.id})

	def coffeeprice(self):
		total = 0
		total += self.bean_type.price
		total += self.roast_type.price
		for syrup in self.syrup_type.all():
			total += syrup.price
		for powder in self.powder_type.all():
			total += powder.price	
		if self.milk:
			milk_price = .25
			total += Decimal(milk_price)
		shots_price = self.shots_number * .5
		total += Decimal(shots_price)
		return Decimal(total)


# class CoffeeBean(models.Model):
# 	arabica = 'ARABICA'
# 	robusta = 'ROBUSTA'
# 	cbt_choices = (
# 		(arabica, 'Arabica'),
# 		(robusta, 'Robusta')
# 	)
# 	coffee_bean = models.CharField(max_length=20, choices=cbt_choices,default=arabica)
# 	bean_price = models.DecimalField(max_digits=4, decimal_places=3)

# 	def __str__(self):
# 		return self.coffee_bean