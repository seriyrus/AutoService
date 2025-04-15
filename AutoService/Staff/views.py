from django.shortcuts import render, redirect
from .forms import CreateStaffForm
from .models import Staffs



def Staff(request):
    form = CreateStaffForm()
    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.save()
            return redirect(request.path)
        else:
            form = CreateStaffForm()
    
    staff = Staffs.objects.all()
    data = {
        'Title':'Staff',
        'form': form,
        'StaffList':staff,
    }
    return render(request, 'Staff/Staff.html', data)