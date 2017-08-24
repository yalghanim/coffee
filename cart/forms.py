from django import forms
from arabica.models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = "__all__"
		exclude = ['user']


class AddressSelectForm(forms.Form):
	address = forms.ModelChoiceField(
		queryset = Address.objects.all(),
		)