from django.shortcuts import render, get_object_or_404
from .models import Meeting, Resource
from .forms import MeetingForm,ResourceForm
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

##form views
def newMeeting(request):
	form=MeetingForm

	if request.method=='POST':
		form=MeetingForm(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=MeetingForm
	else:
		form=MeetingForm()
	return render(request, 'pythonClubApp/newmeeting.html', {'form':form})

def newResource(request):
	form=ResourceForm

	if request.method=='POST':
		form=ResourceForm(request.POST)
		if form.is_valid():
			post=form.save(commit=True)
			post.save()
			form=ResourceForm
	else:
		form=ResourceForm()
	return render(request, 'pythonClubApp/newresource.html', {'form':form})
