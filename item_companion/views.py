from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Items

def home(req):
	return render(req, 'item_companion/home.html')

'''
Return the name of all items
'''
def all_items(req):
	items = [ str(item.name) for item in Items.objects.all() ]
	return JsonResponse({'items' : items})