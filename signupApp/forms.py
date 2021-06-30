from django import forms

class registerForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=200, required=True)
    lastName = forms.CharField(label='Last Name', max_length=200, required=True)
    age = forms.IntegerField(label="Age", required=True, min_value=0, max_value=20)
    pickupName = forms.CharField(label='Pickup Person', max_length=200, required=True)
    parentLocation = forms.CharField(label='Parent Minyan', max_length=200, required=True)
    allergies = forms.CharField(label='Allergies', max_length=200, required=False)
    address = forms.CharField(label='Home Address', max_length=200, required=True)
