from django.shortcuts import render
from .forms import FormUser
from django.http import HttpResponseRedirect

def register_name(request):
    if request.method == "post":
        form = FormUser(request.post)
        print(form.cleaned_data())
        if form.is_valid:
            return HttpResponseRedirect('/blog/')
    else:
        form = FormUser()


    return render(request,'HomePage/Home.html',{'form' : form})
