from django.db import models
from django.contrib.auth.models import User

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
	water = models.FloatField()
	milk = models.BooleanField(default=False)
	foam = models.FloatField()
	extra_instructions = models.TextField()
	price = models.DecimalField(max_digits=4, decimal_places=3)
	completed = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name



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