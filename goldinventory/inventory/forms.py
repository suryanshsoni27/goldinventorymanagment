from django import forms
from .models import *
# add forms to put new data in the database


class earringForm(forms.ModelForm):
    class Meta:
        model = earring
        fields = ('id', 'type', 'price', 'issues', 'status')


class ringForm(forms.ModelForm):
    class Meta:
        model = rings
        fields = ('id', 'type', 'price', 'issues', 'status')


class diamondForm(forms.ModelForm):
    class Meta:
        model = diamonds
        fields = ('id', 'type', 'price', 'issues', 'status')
