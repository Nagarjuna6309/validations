from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def brock(request):
    form=NameForm()
    d={'form':form}
    if request.method=="POST":
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'brock.html',d)