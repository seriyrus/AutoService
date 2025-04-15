from django.shortcuts import redirect, render
from .models import Property as Prop
from .forms import CreatePropForm, PropFilters
from django.db.models import Q, F

def Property(request):
    form = CreatePropForm()
    props = Prop.objects.all()
    filtersForm = PropFilters(request.POST)
    if request.method == 'POST' and 'prop_name' in request.POST:
        print("Добавить")
        form = CreatePropForm(request.POST)
        if form.is_valid():
            property, Created = Prop.objects.get_or_create(
                prop_name = form.cleaned_data['prop_name'],
                prop_cost = form.cleaned_data['prop_cost'],
                defaults={
                    'prop_col':form.cleaned_data['prop_col'],
                    'prop_position':form.cleaned_data['prop_position']}
                )
            print(Created)
            if not Created:
                print("Уже существует")
                Prop.objects.filter(prop_name = property.prop_name).update(prop_col = F('prop_col') + form.cleaned_data['prop_col'])
                form = CreatePropForm()
                redirect("Property:Property")
            else:
                print("Создаем новый")
                property.save()
                form = CreatePropForm()
                redirect("Property:Property")
        else:
            form = CreatePropForm()
            
    if request.method == 'POST' and 'Prop_Name' in request.POST:
        print("Искать")
        if filtersForm.is_valid():
            print('Форма верная')
            name_form = filtersForm.cleaned_data["Prop_Name"]
            cost_form = filtersForm.cleaned_data["Prop_Cost"]
            col_form = filtersForm.cleaned_data["Prop_Col"]
            fil = Q()
            print('Создаем фильтры')
            if name_form:
                fil &= Q(prop_name__icontains = name_form.lower())
            if cost_form:
                fil &= Q(prop_cost = cost_form)
            if col_form:
                fil &= Q(prop_col__lte = col_form)
                
            props =props.filter(fil)
            return render(request, 'Property/Property.html', {
        "Title":"Склад",
        'props':props,
        'form': form,
        'FiltersForm':filtersForm,
    }   )
        else:
            filtersForm = PropFilters()
            form = CreatePropForm()

    for prop in props:
        try:
            prop.prop_allcost = prop.prop_col * prop.prop_cost
        except:
            prop.prop_allcost = 0
        
    
    data = {
        
        'props':props,
        'Title':"Склад",
        'form': form,
        'FiltersForm':filtersForm,
    }
    return render(request, 'Property/Property.html', data)