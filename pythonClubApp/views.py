from django.shortcuts import render
from .models import Resource
# Create your views here.
def index(request):
	return render(request, 'pythonClubApp/index.html')

def resources(request):
	resourceList = Resource.objects.all()
	return render(request, 'pythonClubApp/resources.html', {'resourceList': resourceList})