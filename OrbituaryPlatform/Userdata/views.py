from django.shortcuts import render

# Create your views here.
from .models import Userdata
from .forms import UserDataForm


def userdata_database_view(request):
    obj = Userdata.objects.get(id=2)
    context = {
        'object': obj
    }   
    return render(request, 'userdata/userdataDetail.html', context)

def userdata_create_view(request):
    form = UserDataForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserDataForm()   
    context = {
        'form': form
    }   
    return render(request, 'userdata/userdataCreate.html', context)