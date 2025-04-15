from django import forms
from .models import Staffs
from colorfield.forms import ColorField

class CreateStaffForm(forms.ModelForm):
    staff_job = forms.CharField(label="Должность", max_length=40, widget=forms.TextInput(attrs={'class':'CreateStaffFormJob'}))
    staff_name = forms.CharField(label="Имя", max_length=150, widget=forms.TextInput(attrs={'class':'CreateStaffFormName'}))
    staff_surname = forms.CharField(label="Фамилия", max_length=150, widget=forms.TextInput(attrs={'class':'CreateStaffFormSurname'}))
    color = ColorField(label="Цвет", initial="#FF0000")
    class Meta:
        model = Staffs
        fields = "__all__"