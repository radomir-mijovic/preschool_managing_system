from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class UpdatePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
