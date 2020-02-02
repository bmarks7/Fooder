from django.shortcuts import render
from .forms import FoodItemForm, NumItemsForm
from .models import FoodItem, Food
from django.forms import formset_factory

rec_kcal = 2600
rec_protein = 52
rec_lipid = 65
red_carbohydrt = 117
rec_fiber = 33.6
rec_calcium = 1000
rec_iron = 8
rec_potassium = 4700
rec_sodium = 2300
rec_vic_c = 45
rec_vit_b12 = 6
rec_vit_a_iu = 5000
rec_vit_e = 10
rec_vit_d = 120

rec_vars = [rec_kcal,
rec_protein,
rec_lipid,
red_carbohydrt,
rec_fiber,
rec_calcium,
rec_iron,
rec_potassium,
rec_sodium,
rec_vic_c,
rec_vit_b12,
rec_vit_a_iu,
rec_vit_e,
rec_vit_d] 

nutri_vars = ['Energy_Kcal', 'Protein', 'Lipid', 'Carbohydrate', 
			'Fiber', 'Calcium', 'Iron', 'Potassium', 'Sodium',
			'Vitamin C', 'Vitamin B12', 'Vitamin A', 'Vitamin E', 'Vitamin D']

nutri_vars_meas = ['', 'g', 'g', 'g', 
			'g', 'mg', 'mg', 'mg', 'mg',
			'mg', 'µg', '', 'mg', 'µg']

def home(request):
	num_items_form = NumItemsForm()
	return render(request, 'bill/home.html', {'num_items_form': num_items_form})


def enter_food_items(request):
	num_items = 1
	multiple_items_form = NumItemsForm(request.GET)
	if multiple_items_form.is_valid():
		num_items = multiple_items_form.cleaned_data['num_items']

	Item_Form_Set = formset_factory(FoodItemForm, extra = num_items)
	formset = Item_Form_Set

	results = 'According to the recommended nutrition by Statistics Canada:\n'
	if request.method == 'POST':
		filled_formset = Item_Form_Set(request.POST)
		if filled_formset.is_valid():
			note = 'Items have been recorded'

			for form in filled_formset:
				food = form.cleaned_data['name']
				form_vars = [food.Energy_Kcal, 
				food.Protein * (form.cleaned_data['amount']/15), 
				food.Lipid_Tot * (form.cleaned_data['amount']/15), 
				food.Carbohydrt * (form.cleaned_data['amount']/15), 
				food.Fiber_TD * (form.cleaned_data['amount']/15), 
				food.Calcium * (form.cleaned_data['amount'] * 1000/15), 
				food.Iron * (form.cleaned_data['amount'] * 1000/15), 
				food.Potassium * (form.cleaned_data['amount'] * 1000/15), 
				food.Sodium * (form.cleaned_data['amount'] * 1000/15), 
				food.Vit_C * (form.cleaned_data['amount'] * 1000/15), 
				food.Vit_B12 * (form.cleaned_data['amount'] * 1000000/15), 
				food.Vit_A, 
				food.Vit_E * (form.cleaned_data['amount'] * 1000/15), 
				food.Vit_D * (form.cleaned_data['amount'] * 1000000/15)]

				for i in range(len(form_vars)):
					if rec_vars[i] > form_vars[i]:
						results = results + '- You are ' + str(rec_vars[i] - form_vars[i]) + ' ' + str(nutri_vars_meas[i]) + ' too short of ' + str(nutri_vars[i]) + '\n'
					elif rec_vars[i] < form_vars[i]:
						results = results + '- You are ' + str(form_vars[i] - rec_vars[i]) + ' ' + str(nutri_vars_meas[i]) + ' too high in ' + str(nutri_vars[i]) + '\n'
					elif rec_vars[i] == form_vars[i]:
						results = results + '- You have the exact recommended amount of ' + str(form_vars[i]) + '\n'

				form.save()


		else:
			note = 'Please try again'
		return render(request, 'bill/enter_food_items.html', {'note': note, 'formset': formset, 'results': results})
	else:
		return render(request, 'bill/enter_food_items.html', {'formset': formset})

def analysis(request):
	if request.method == 'POST':
		filled_formset = ItemFormSet(request.POST)

		for form in filled_formset:
			form.bill = filled_bill_form

		if filled_formset.is_valid():
			for form in filled_formset:
				form.save()
			note = 'Your items have been recorded'
		else:
			note = 'Items have not been recorded'
		return render(request, 'bill/enter_food_items.html', {'note': note, 'formset': formset})