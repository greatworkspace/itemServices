from django.db import models

# Create your models here.
class Products(models.Model):
	category = models.CharField(max_length = 250)
	group = models.CharField(max_length = 250)
	sub_group = models.CharField(max_length = 250)
	brand_name = models.CharField(max_length = 100)
	#quantity = model.
	item = models.CharField(max_length = 100)

	def __str__(self):
		return self.item