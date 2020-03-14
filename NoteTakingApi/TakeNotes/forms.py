from django import forms
from TakeNotes.models import UserProfileInfo,TakeNotes
from django.contrib.auth.models import User
import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site',)

class TakeNotesForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    Note_id = forms.CharField(max_length=255)
    Add_notes = forms.CharField(
    required = True,  
    widget = forms.TextInput())
    created = forms.DateField(initial=datetime.date.today)
    class Meta():
        model = TakeNotes
        fields = ['title','Note_id','Add_notes']