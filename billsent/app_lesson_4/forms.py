from django import forms
from django.contrib.auth import get_user_model
from django contrib.auth.forms import UserCreationForm
from app_billsent.models import Billsent

User = get_user_model()

class ExtendedUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        model = Billsent
        fields = ['pub_date', 'headline', 'content', 'reporter']