from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForm

# Create your views here.
def Home(req): 
    tasks=Task.objects.all()
    if req.method=="POST":
        
        task=req.POST.get('task','')
        priority=req.POST.get('priority','')
        date=req.POST.get('date','')
        img=req.FILES['image']        
        todo=Task(task=task,priority=priority,date=date,image=img)
        todo.save()
    return render(req,'index.html',{"tasks":tasks})

def Update(req,id):
    tasks=Task.objects.get(id=id)
    # if req.method=="POST":
    #     task=req.POST.get('task','')
    #     priority=req.POST.get('priority','')
    #     Task.objects.filter(id=id).update(task=task,priority=priority)
    #     return redirect("home")
    # ==================================================================
    # django forms
    f=TodoForm(req.POST or None,instance=tasks)
    if f.is_valid():
        f.save()
        return redirect("home")
    # return render(req,'update.html',{"task":tasks})
    return render(req,'formUpdate.html',{"task":tasks,'f':f})


def Delete(req,id):
    tasks=Task.objects.get(id=id)
    if req.method=="POST":
        Task.objects.filter(id=id).delete()
        return redirect("home")
    return render(req,'delete.html',{"task":tasks})