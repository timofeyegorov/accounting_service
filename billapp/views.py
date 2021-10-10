from django.shortcuts import render
from billapp.descriptions import descriptions_list
from .models import Operation
from .forms import OperationForm
import numpy as np

# Create your views here.
def main_view(request):
    descriptions = descriptions_list
    description = np.random.choice(descriptions)
    operations = Operation.objects.all()
    return render(request, 'billapp/index.html', context={'description': description, 'operations': operations})

# def enter_expenses(request):
#     return render(request, 'billapp/enter.html')

def enter_expenses(request):
    new_operation = OperationForm()
    if request.method == 'POST':
        new_operation = OperationForm(request.POST)
        if new_operation.is_valid():
            new_operation.save()
            return render(request, 'billapp/success.html', context = {'new_operation': new_operation})
    return render(request, 'billapp/enter.html', context = {'new_operation': new_operation})

def contacts(request):
    return render(request, 'billapp/contacts.html')