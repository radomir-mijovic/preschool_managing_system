from django import forms
from .models import Payment, Teachers, Kids


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = '__all__'


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teachers
        fields = '__all__'


class UpdatePaymentForm(forms.ModelForm):

    bank_paper_id = forms.IntegerField(label='BROJ IZVODA')
    payment_date = forms.CharField(label='DATUM UPLATE')
    paid = forms.FloatField(label='UPLACENO')
    need_to_pay = forms.FloatField(label='TREBA DA UPLATI')
    notes = forms.CharField(label='NAPOMENA')

    class Meta:
        model = Payment
        fields = '__all__'
