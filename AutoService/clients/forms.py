from django import forms
from .models import Clients


class CreateClientForm(forms.ModelForm):
    client_name = forms.CharField(label="Имя", max_length=150, widget=forms.TextInput(attrs={'class':'CreateClientFormName'}))
    client_surname = forms.CharField(label="Фамилия", max_length=150, widget=forms.TextInput(attrs={'class':'CreateClientFormSurname'}))
    client_fathername = forms.CharField(label="Отчество", max_length=150, widget=forms.TextInput(attrs={'class':'CreateClientFormFathername'}))
    client_phone = forms.CharField(label="Телефон", max_length=20, widget=forms.TextInput(attrs={'class':'CreateClientFormPhone'}))
    client_auto = forms.CharField(label="Авто", max_length=500, widget=forms.Textarea(attrs={'class':'CreateClientFormAuto'}))
    class Meta:
        model = Clients
        fields = "__all__"