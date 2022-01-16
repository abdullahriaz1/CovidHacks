from django.forms import ModelForm
from .models import Guest, Event

class GuestForm(ModelForm):
	class Meta:
		model = Guest
		fields = '__all__'
  
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        