from django import forms
from .models import Operation

class OperationForm(forms.ModelForm):
    operation_sum = forms.FloatField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Сумма', 'class': 'form-control'}))
    people_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))
    operation_type = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Тип операции', 'class': 'form-control'}))
    operation_tag = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Назначение', 'class': 'form-control'}))
    class Meta:
        model = Operation
        fields = '__all__'
