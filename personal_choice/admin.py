from django.contrib import admin
from .models import *

'''cutomized admin panel, so you can easily search customer_info by using your customer_info'''
class customer_infoAdmin(admin.ModelAdmin):
	list_display = ('customer_name','gender','nid','age')
	list_display_links = ('customer_name','nid')
	list_filter = ('nid','customer_name')
	search_fields = ('nid','customer_name')
	list_per_page = 25

'''cutomized admin panel, so you can easily see list of the owner,
pet and per color and 
also can edit by just clicking on owner_name or pet_name and also can filter'''
class pet_infoAdmin(admin.ModelAdmin):
	list_display = ('owner_name','pet_name','pet_color')
	list_display_links = ('owner_name','pet_name')
	list_filter = ('owner_name','pet_name',)
	list_per_page = 25


admin.site.register(customer_info, customer_infoAdmin)
admin.site.register(pet_info, pet_infoAdmin)
admin.site.register(color)

