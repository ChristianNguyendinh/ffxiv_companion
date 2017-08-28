from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Items

def home(req):
	return render(req, 'item_companion/home.html')

'''
Return info about a single item
'''
def single_item(req, itemname):
	item_formatted = itemname.replace('_', ' ')

	try:
		itemObj = Items.objects.get(name=item_formatted)
		item = {
			'item_name'	: str(itemObj.name), 
			'main_type'	: str(itemObj.main_type),
			'sub_type'	: str(itemObj.sub_type),
			'img_url'	: str(itemObj.img),
			'item_lvl'	: str(itemObj.ilvl),
			'req_lvl'	: str(itemObj.rlvl),
		}
	except:
		item = { 'error': 'item: \'' + item_formatted + '\' - not found. Check case sensitivity!' }

	return JsonResponse(item)

'''
Return the name of all items
'''
def all_item_names(req):
	items = [ { 'value': str(item.name) } for item in Items.objects.all() ]
	return JsonResponse({ "suggestions": items })

'''
Return info about all materials only
'''
def all_material_names(req):
	materials = [ { 'value': str(item.name) } for item in Items.objects.filter(main_type="Materials") ]
	return JsonResponse({ "suggestions": materials })

'''
Return all info about all items
'''
def all_item_full(req):
	items = [ 
		{ 
			'value'		: str(item.name), 
			'main_type'	: str(item.main_type),
			'sub_type'	: str(item.sub_type),
			'img_url'	: str(item.img),
			'item_lvl'	: str(item.ilvl),
			'req_lvl'	: str(item.rlvl),
		} for item in Items.objects.all() 
	]
	return JsonResponse({ "suggestions": items })
