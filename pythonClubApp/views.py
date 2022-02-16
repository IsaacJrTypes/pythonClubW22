from django.shortcuts import render, get_object_or_404
from .models import Meeting, Resource
# Create your views here.
def index(request):
	return render(request, 'pythonClubApp/index.html')

def resources(request):
	resourceList = Resource.objects.all()
	return render(request, 'pythonClubApp/resources.html', {'resourceList': resourceList})

def meetings(request):
	meetingList=Meeting.objects.all()
	return render(request,'pythonClubApp/meetings.html', {'meetingList': meetingList})

def meetingDetails(request,id):
	meeting=get_object_or_404(Meeting,pk=id)
	return render(request,'pythonClubApp/meetingdetails.html', {'meeting': meeting})

