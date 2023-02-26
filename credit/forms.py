from django import forms
from django.forms import ModelForm
from .models import Credit, Customer

class CreditForm(ModelForm):
    class Meta:
        model = Credit
        fields= ['customer',
                 'description', 'amount_credit']
        labels = {
			'name': 'Customer',
			'description': 'Item',
			'amount_credit': 'Amount credit',	
		}

        widgets = {
			'name': forms.Select(attrs={'class':'form-select', 'placeholder':'Customer'}),
			'description': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Item'}),
			'amount_credit': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Amount_Credit'}),	
		}

class CreateCreditForm(ModelForm):
	class Meta:
		model = Credit
		fields = [
			'customer',
			'created_by',
			'description',
			'amount_credit',
		]