from django import forms
from .models import Sondage, DateSondage

class SondageForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    heure = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Sondage
        fields = ['name', 'lieux', 'date', 'heure']

class DateSondageForm(forms.Form):
    date_1 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_2 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_3 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DateSondage
        fields = ['date_1', 'date_2', 'date_3']

class VoteForm(forms.Form):
    def _init_(self, sondage, *args, **kwargs):
        super(VoteForm, self)._init_(*args, **kwargs)
        dates_sondage = DateSondage.objects.filter(sondage=sondage)
        for date in dates_sondage:
            self.fields[f"date_{date.id}"] = forms.BooleanField(required=False, label=date.date)
            self.fields[f"percentage_{date.id}"] = forms.IntegerField(initial=0, widget=forms.HiddenInput())