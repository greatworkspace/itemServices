from django.db import models
#from django.utils import timezone

# Create your models here.
class Product(models.Model):
	PRODUCTS_CATEGORIES = [
		('Drinks', 'Drinks'),
		('Pharma_Prod', 'Pharmaceuticals Product'),
		('C_A','Children Accessories'),
		('HB_Prod','Health and Beauty Products'),
		('MW_Acc','Men and Women Accessories'),
		('STATS', 'Stationery'),
		('D_Prod','Dairy Product'),
		('S_S','Sweets and Snacks'),
	]

	product_category = models.CharField(max_length = 50, verbose_name='Product Category', choices = PRODUCTS_CATEGORIES)
	item_name = models.CharField(max_length = 120, verbose_name = 'Item Name')
	#item_barcode = models.CharField(max_length = 15)
	description = models.TextField(blank = False,  verbose_name = 'Product Description')
	frac = models.IntegerField(default = 1)
	purchasing_price = models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Price in Naira')
	purchasing_unit = models.PositiveIntegerField(verbose_name = 'purchasing unit in pcs')
	sales_price = models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Price in Naira')
	sales_unit = models.PositiveIntegerField(verbose_name = 'sales unit in pcs')
	#create_ts = models.DateTimeField(default = timezone.now, editable=True)
		

	def __str__(self):
		return self.item_name

