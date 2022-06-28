from django.shortcuts import render
from .models import ToDo
# Create your views here.

def show_todo(request):
    todos = ToDo.objects.all()
    return render(request, 'main.html', {'todos':todos})


def create_todo(request):
    if request.method == 'GET':
        return render(request, 'create_from_user.html')
    else:
        description = request.POST.get('description')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        todo = ToDo.objects.create(description=description, status=status, deadline=deadline)
        context = {'todo': todo}
        return render(request, 'new_todo.html',context)

def show_details(request,pk):
    todo = ToDo.objects.get(pk=pk)
    return render(request, 'detail.html',{'todo': todo})