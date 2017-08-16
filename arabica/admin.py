from django.contrib import admin
from arabica.models import * 


class RoastAdmin(admin.ModelAdmin):
	list_display = ["roast_type", "price"]
	list_filter = ["roast_type"]
	class Meta:
		model = Roast

class SyrupAdmin(admin.ModelAdmin):
	list_display = ["syrup_type", "price"]
	list_filter = ["syrup_type"]
	class Meta:
		model = Syrup

class PowderAdmin(admin.ModelAdmin):
	list_display = ["powder_type", "price"]
	list_filter = ["powder_type"]
	class Meta:
		model = Powder

class CoffeeBeanAdmin(admin.ModelAdmin):
	list_display = ["bean_type", "price"]
	list_filter = ["bean_type"]
	class Meta:
		model = CoffeeBean

# class CoffeeAdmin(admin.ModelAdmin):
# 	list_display = ["name", "bean_type", "roast_type", "shots_number", "syrup_type", "powder_type", "water", "milk", "foam", "extra_instructions", "price", "completed"]
# 	list_filter = ["name", "bean_type", "roast_type", "syrup_type", "powder_type"]
# 	class Meta:
# 		model = CoffeeBean

admin.site.register(Roast, RoastAdmin)
admin.site.register(Syrup, SyrupAdmin)
admin.site.register(Powder, PowderAdmin)
admin.site.register(CoffeeBean, CoffeeBeanAdmin)
admin.site.register(Coffee)


