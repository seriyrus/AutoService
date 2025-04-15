from django.db.models import F, Q
from django.shortcuts import render, redirect
from .models import Tasks, PropertyTasks
from .forms import CreateTaskForm, TaskFilters, PropertyTasksForm
from Property.models import Property
from django.contrib import messages

def Dashboard(request):
    
    ActiveTasks = Tasks.objects.filter(mode="active")
    activeStaff = []
    for Staff in ActiveTasks:
        activeStaff.append(Staff.staff)
    
    data = {
        'Title':'Дашборд',
        "ActiveTasks": ActiveTasks,
        "ActiveStaff":set(activeStaff),
    }
    return render(request, 'Dashboard/Dashboard.html', data)


def createTask(request):
    
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            newTask = form.save(commit=False)
            newTask.save()
            form.save_m2m()
            return redirect("Dashboard:Dashboard")
        else:
            form = CreateTaskForm()
    
    data = {
        'Title':'Создать работу',
        'form': form,
    }
    return render(request, 'Dashboard/CreateTask.html', data)


def checkTask(request, pk):

    ct=Tasks.objects.get(id=pk)
    
    form1 = CreateTaskForm(instance=ct)
    form2 = PropertyTasksForm()
    
    if request.method == 'POST' and "count" in request.POST:
        form2 = PropertyTasksForm(request.POST)
        if form2.is_valid():
            newPropToTask = form2.save(commit=False)
            newPropToTask.save()
            task = Tasks.objects.get(id=pk)
            task.props.add(newPropToTask)
            getproplst = str(form2.cleaned_data.get('prop')).split(':')[0]
            print(getproplst)
            propFromTask = Property.objects.get(prop_name=getproplst)
            existcol = propFromTask.prop_col
            if int(existcol)-int(form2.cleaned_data['count']) < 0:
                return messages.info(request, 'Недостаточно деталей на складе!')
            else:
                propFromTask.prop_col-=int(form2.cleaned_data['count'])
                form2 = PropertyTasksForm()
                propFromTask.save()
                task.save()
                return redirect("Dashboard:Dashboard")
        else:
            form2 = PropertyTasksForm()
    if request.method == "POST" and 'works' in request.POST:
        form1 = CreateTaskForm(request.POST)
        if form1.is_valid():
            Tasks.objects.filter(id=pk).update(staff = form1.cleaned_data.get('staff'), 
                    client = form1.cleaned_data.get('client'),
                    price = form1.cleaned_data.get('price'), mode = form1.cleaned_data.get('mode'),
                    works = form1.cleaned_data.get('works'))
            return redirect("Dashboard:Dashboard")
        else:
            form1 = CreateTaskForm()
    
    data = {
        "Title":"checkTask",
        "form1":form1,
        "form2":form2,
    }
    return render(request, 'Dashboard/checkTask.html', data)

def AllTasks(request):
    
    task = Tasks.objects.all()
    filtersForm = TaskFilters(request.POST)
    if request.method == "POST":
        if filtersForm.is_valid():
            staff_form = filtersForm.cleaned_data["formstaff"]
            client_form = filtersForm.cleaned_data["formclient"]
            works_form = filtersForm.cleaned_data["formworks"]
            fil = Q()
                
            if staff_form:
                fil &= Q(staff = staff_form)
            if client_form:
                fil &= Q(client = client_form)
            if works_form:
                fil &= Q(works__icontains = works_form)
                
            task =task.filter(fil)
            return render(request, 'Dashboard/AllTasks.html', {
        "Title":"Все работы",
        "tasks":task,
        "form":filtersForm,
    }   )
        else:
            filtersForm = TaskFilters() 
    
    return render(request, 'Dashboard/AllTasks.html', {
        "Title":"Все работы",
        "tasks":task,
        "form":filtersForm,
    }   )