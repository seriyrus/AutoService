from django import forms
from .models import Property
from .models import Property


class CreatePropForm(forms.ModelForm):
    prop_name = forms.CharField(label="Наименование", max_length=150, widget=forms.TextInput(attrs={'class':'CreatePropFormName'}))
    prop_cost = forms.IntegerField(label="Стоимость", widget=forms.TextInput(attrs={'class':'CreatePropFormCost'}))
    prop_col = forms.IntegerField(label="Количество", widget=forms.TextInput(attrs={'class':'CreatePropFormCol'}))
    prop_position = forms.CharField(label="Место на складе",max_length=40, widget=forms.TextInput(attrs={'class':'CreatePropPosition'}))
    class Meta:
        model = Property
        fields = ["prop_name", "prop_cost", "prop_col", "prop_position"]
        
        
class PropFilters(forms.ModelForm):
    Prop_Name = forms.CharField(label="Наименование" ,max_length=1000, widget=forms.TextInput(attrs={"class":"FilterPropsName"}),required=False)
    Prop_Cost = forms.CharField(label="Стоимость" ,max_length=1000, widget=forms.TextInput(attrs={"class":"FilterPropsCost"}),required=False)
    Prop_Col = forms.CharField(label="Количество" ,max_length=1000, widget=forms.TextInput(attrs={"class":"FilterPropsCol"}),required=False)
    class Meta:
        model = Property
        fields = ["Prop_Name", "Prop_Cost", "Prop_Col"]