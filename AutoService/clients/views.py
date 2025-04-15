from django.shortcuts import render, redirect
from .models import Clients
from .forms import CreateClientForm

def clients(request):
    form = CreateClientForm()
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()

            return redirect(request.path)
        else:
            form = CreateClientForm()
    
    cclients = Clients.objects.all()
    data = {
        'Title':'Клиенты',
        'form': form,
        'ClientList':cclients,
    }
    return render(request, 'clients/clients.html', data)
