
from django import forms


from .models import Hero

class InputForm(forms.ModelForm):
	class Meta:
		model = Hero
		exclude = ['age']

# class OutputForm(forms.ModelForm):
#     class Meta:
#         model = Hero
#         fields = ['age',]
