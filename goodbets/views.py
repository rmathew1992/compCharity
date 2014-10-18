from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse
from django.shortcuts import render
from goodbets.models import User
def index(request):
    return TemplateResponse(request,'index.html')

def profile(request):
	if request.method == 'GET':
		# print('Request body', request.GET)
		name = request.GET.__getitem__('last_name') + ' ' + request.GET.__getitem__('first_name')
		print('Name: ', name )
		if not User.objects.filter(username=name):
			User(username=name, id="0").save()
		return render(request,'profile.html')