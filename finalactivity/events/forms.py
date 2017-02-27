from django import forms
from events.models import Events

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        #fields = ('title','brief_intro','poster','organizer','contact_email','contact_phonenumber','capacity','age_limit','ticket','description','starttime','endtime','music','sports','food','party','arts','business','location')
        fields = ('title','brief_intro','poster','organizer','contact_email','contact_phonenumber','capacity','age_limit','ticket','description','starttime','endtime','music','sports','food','party','arts','business')

