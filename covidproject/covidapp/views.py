from django.shortcuts import render

# Create your views here.
from .models import Guest, Event
from rest_framework import viewsets
from rest_framework import permissions
from covidapp.serializers import GuestSerializer, EventSerializer
from covidapp.forms import GuestForm, EventForm
    
class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    
def indexGuest(request):

	form = GuestForm()

	if request.method == 'POST':
		form = GuestForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'app/indexGuest.html', context)

def indexEvent(request):

	form = EventForm()

	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'app/indexEvent.html', context)

def eventPage(request):
    pass