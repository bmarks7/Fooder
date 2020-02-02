from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
	class Meta:
		model = FoodItem
		fields = ['name', 'amount']
		labels = {'name': 'Name', 'amount': 'Amount(grams)'}

class NumItemsForm(forms.Form):
	num_items = forms.IntegerField(min_value=1)