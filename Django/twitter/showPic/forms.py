from django import forms

class getUser(forms.Form):
    user = forms.CharField(max_length=20)

