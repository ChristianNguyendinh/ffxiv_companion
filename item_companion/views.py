from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Items

def home(req):
	return render(req, 'item_companion/home.html')

'''
Return the name of all items
'''
def all_item_names(req):
	items = [ { 'value': str(item.name) } for item in Items.objects.all() ]
	return JsonResponse({ "suggestions": items });

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
	return JsonResponse({ "suggestions": items });