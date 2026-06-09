from django import forms

class AddForm(forms.Form):
    value1 = forms.IntegerField()
    value2 = forms.IntegerField()