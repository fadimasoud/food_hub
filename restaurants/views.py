from django.shortcuts import render
from .models import Restaurant
def restaurant_list(request):
	objects= Restaurant.objects.all()
	context = {
		"objects":objects,
	}
	return render(request, 'list.html', context)


def restaurant_detail(request, food_id):
	objects= Restaurant.objects.get(id=food_id)
	context = {
		"objects":objects,
	}
	return render(request, 'detail.html', context)
