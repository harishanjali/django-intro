from django import forms

class Addition(forms.Form):
    value1 = forms.IntegerField()
    value2 = forms.IntegerField()
    date = forms.DateField(widget=forms.SelectDateWidget)
    print("in addition")

  
        