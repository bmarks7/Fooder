from django.db import models
from django.core.validators import MinValueValidator



class Food(models.Model):
	name = models.CharField(max_length = 100)
	Energy_Kcal = models.FloatField()
	Protein = models.FloatField()
	Lipid_Tot = models.FloatField()
	Carbohydrt = models.FloatField()
	Fiber_TD = models.FloatField()
	Calcium = models.FloatField()
	Iron = models.FloatField()
	Potassium = models.FloatField()
	Sodium = models.FloatField()
	Vit_C = models.FloatField()
	Vit_B12 = models.FloatField()
	Vit_A = models.FloatField()
	Vit_E = models.FloatField()
	Vit_D = models.FloatField()


	def __str__(self):
		return self.name

class FoodItem(models.Model):
	name = models.ForeignKey(Food, on_delete = models.CASCADE)
	amount = models.FloatField()

	def __str__(self):
		return self.name + ' - ' + str(self.amount) + 'g'