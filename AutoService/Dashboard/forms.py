from django import forms
from .models import Tasks, PropertyTasks
from Staff.models import Staffs
from clients.models import Clients
from Property.models import Property

class CreateTaskForm(forms.ModelForm):
    staff = forms.ModelChoiceField(label="Сотрудник", queryset=Staffs.objects.all())
    client = forms.ModelChoiceField(label="Клиент", queryset=Clients.objects.all())
    price = forms.CharField(label="Цена", max_length=100, widget=forms.TextInput(attrs={"class":"Price"}))
    mode = forms.ChoiceField(label="Состояние", choices=Tasks.CHOISES)
    works = forms.CharField(label="Работы", max_length=1000, widget=forms.Textarea(attrs={"class":"Works"}))
    class Meta:
        model = Tasks
        fields = ["staff","client","price","mode","works"]
        
        
class TaskFilters(forms.ModelForm):
    formstaff = forms.ModelChoiceField(label="Сотрудник", queryset=Staffs.objects.all(), required=False)
    formclient = forms.ModelChoiceField(label="Клиент", queryset=Clients.objects.all(),required=False)
    formworks = forms.CharField(label="Работы", widget=forms.TextInput(attrs={"class":"FilterWorks"}),required=False)
    class Meta:
        model = Tasks
        fields = ['formstaff', 'formclient', 'formworks']
        
        
class PropertyTasksForm(forms.ModelForm):
    Props = Property.objects.all()
    count = forms.CharField(label = "Количество ", max_length=5, widget=forms.TextInput(attrs={"class":"countform"}))
    prop = forms.ModelChoiceField(label = "Детали ", queryset=Props) #""" , attrs={"class":"countform"})) """
    class Meta:
        model = PropertyTasks
        fields = "__all__"