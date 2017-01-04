from django.shortcuts import render
from .forms import PersonForm
# Create your views here.
def index(request):
        return render(request,'personal/home.html')

def new_person(request):
        if request.method == "POST":
                form = PersonForm(request.POST)
                if form.is_valid():
                        post = form.save(commit=False)
                        post.save()
        else:
                form  = PersonForm()
        return render(request,'personal/home.html',{'form':form})
