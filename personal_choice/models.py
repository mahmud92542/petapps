from django.db import models


'''new section for adding customer information.'''
class customer_info(models.Model):
	customer_name = models.CharField(max_length=100,unique=True)
	gender_choice = ('M','Male'),('F','Female')
	gender = models.CharField(max_length=6, choices=gender_choice)
	nid = models.IntegerField(unique=True)
	age = models.IntegerField()

	def __str__(self):
		return self.customer_name

'''add color,don't delete any color!!!'''
class color(models.Model):
	color = models.CharField(max_length=20)

	def __str__(self):
		return self.color

'''pet info'''
class pet_info(models.Model):
	owner_name = models.OneToOneField(customer_info, on_delete=models.CASCADE) 
	#if you delete customer_name from customer_info you're pet info will delete.
	pet_name = models.CharField(max_length=100, unique=True)
	pet_color = models.OneToOneField(color,on_delete=models.CASCADE)

	def __str__(self):
		return self.pet_name

