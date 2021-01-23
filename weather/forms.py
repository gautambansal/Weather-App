from django import forms


class CityForm(forms.Form):
    city_name = forms.CharField(widget = forms.TextInput(attrs={'class':'input', 'placeholder':'City Name','size': '40'}))
    