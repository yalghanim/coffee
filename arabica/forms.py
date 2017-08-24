from django import forms
from django.contrib.auth.models import User
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

class UserSignUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email', 'first_name', 'last_name']

		widgets = {
		'password': forms.PasswordInput(),
		'email': forms.EmailInput(),
		}
	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(UserSignUp, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['email'].required = True
		self.fields['first_name'].required = True
	

class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())


class RoastForm(forms.ModelForm):
	class Meta:
		model = Roast
		fields = ['roast_type', 'price']

class SyrupForm(forms.ModelForm):
	class Meta:
		model = Syrup
		fields = ['syrup_type', 'price']

class PowderForm(forms.ModelForm):
	class Meta:
		model = Powder
		fields = ['powder_type', 'price']

class CoffeeBeanForm(forms.ModelForm):
	class Meta:
		model = CoffeeBean
		fields = ['bean_type', 'price']

# class AddressForm(forms.ModelForm):
# 	class Meta:
# 		model = "arabica.Address"
# 		fields = ['name', 'city', 'block', 'street', 'building', 'avenue', 'floor', 'apt_number', 'extra_directions']
# 		# help_texts = {
# 		# 	'extra_instructions': 'Write any extra instructions you might have for us.',
# 		# 	'water': 'in mL',
# 		# 	'foam': 'in mL',
# 		# }
# 		# labels = {
# 		# 	'name': 'Your name',
# 		# 	'bean_type': 'Type of Bean',
# 		# 	'roast_type': 'Degree of Roast',
# 		# 	'shots_number': 'Number of Shots',
# 		# 	'Syrup_type': 'Syrup(s) to add',
# 		# 	'Powder_type': 'Powder(s) to add',
# 		# 	'water': 'How much water to add.',
# 		# 	'milk': 'Milk?',
# 		# 	'foam': 'How much foam to add.',
# 		# }

class CityForm(forms.ModelForm):
	class Meta:
		model = City
		fields = ['name']


class OrderForm(forms.ModelForm):
	class Meta:
		model = Coffee
		fields = ['name', 'bean_type', 'roast_type', 'shots_number', 'syrup_type', 'powder_type', 'water', 'milk', 'foam', 'extra_instructions']
		# fields = '__all__'
		# exclude = ['user', 'price']
		#another way of putting the fields

		help_texts = {
			'extra_instructions': 'Write any extra instructions you might have for us.',
			'water': 'in mL',
			'foam': 'in mL',
		}
		labels = {
			'name': 'Your name',
			'bean_type': 'Type of Bean',
			'roast_type': 'Degree of Roast',
			'shots_number': 'Number of Shots',
			'Syrup_type': 'Syrup(s) to add',
			'Powder_type': 'Powder(s) to add',
			'water': 'How much water to add.',
			'milk': 'Milk?',
			'foam': 'How much foam to add.',
		}
		#put 5 as maximum value
		widgets = {
			'shots_number': forms.NumberInput(attrs={'min': 1,'max': 5}),
		}


	# def __init__(self, *args, **kwargs):
	# 	super(OrderForm, self).__init__(*args, **kwargs)
	# 	self.helper = FormHelper()
	# 	self.helper.form_class = 'form-horizontal'
	# 	self.helper.label_class = 'col-md-3'
	# 	self.helper.field_class = 'col-md-6'

		# self.helper.layout= Layout(
		# 	Div(
		# 			Div('name',css_class='col-sm-8'),
		# 			Div('abv',css_class='col-sm-4'), css_class='row'
		# 		),
		# 	Div(
		# 			Div(FormActions(Submit('submit','Save')), css_class='col-sm-12'),
		# 			css_class='row'
		# 		)
		# 	)

		#main:
		# def __init__(self, *args, **kwargs):
		# 	super(OrderForm, self).__init__(*args, **kwargs)			
		# 	self.helper = FormHelper()
		# 	self.helper.layout = Layout(
		# 		MultiField(
		# 			'How do you want your coffee {{user|title}}?',
		# 			Div(
		# 				'bean_type',
		# 				'roast_type',
		# 				'shots_number',
		# 				'syrup_type',
		# 				'powder_type',
		# 				'water',
		# 				'milk',
		# 				'foam',
		# 			),
		# 		)
		# 	)

			# self.helper.layout= Layout(
			# 	Div(
			# 		Div('name',css_class='col-sm-8'),
			# 		Div('abv',css_class='col-sm-4'), css_class='row'
			# 		),
			# 	Div(
			# 		Div(FormActions(Submit('submit','Save')), css_class='col-sm-12'),
			# 		css_class='row'
			# 		)
			# 	)


# form.helper.form_action = reverse('url_name', args=[event.id])

