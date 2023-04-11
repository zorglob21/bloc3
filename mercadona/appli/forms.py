from django import forms


class FilterForm(forms.Form):
  Pulls = forms.BooleanField()
  Pantalons = forms.BooleanField()
  Chaussures = forms.BooleanField()




class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)