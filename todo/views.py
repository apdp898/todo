from django.shortcuts import render,redirect
from .models import Task
def index(request):
    if request.method=='POST':
        Task.objects.create(title=request.POST['title'])
        return redirect('/')
    return render(request,'todo/index.html',{'tasks':Task.objects.all()})
def complete(request,pk):
    t=Task.objects.get(id=pk);t.completed=True;t.save();return redirect('/')
def delete(request,pk):
    Task.objects.get(id=pk).delete();return redirect('/')
