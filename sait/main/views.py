from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import ToDoItem, ItemList
from django.http import HttpResponseRedirect


def list(request):
    users = User.objects.all()
    if request.user not in users:
        return redirect('/relog/login/')
    itemlist = ItemList.objects.filter(user__username=request.user)
    return render(request, 'list.html', {"itemlist": itemlist, 'users': users})


def main(request, name):
    all_to_do = ToDoItem.objects.filter(to_do_list_item__title=name)
    print(all_to_do)
    username = request.user
    return render(request, 'main.html', {'all_items': all_to_do, 'username': username, 'name': name})


def add_to_do(request, name):
    do = request.POST['content']
    name = ItemList.objects.get(title=name)
    if do != '' and do.strip().isdigit() != True:
        new_item = ToDoItem(to_do_list_item=name, content=do)
        new_item.save()
    return redirect(request.META['HTTP_REFERER'])


def add_item_list(request):
    list = request.POST['content']
    if list != '' and list.strip().isdigit() != True:
        new_item = ItemList(user=request.user, title=list)
        new_item.save()
    return redirect(request.META['HTTP_REFERER'])


def del_item_list(request, i):
    delete = ItemList.objects.get(id=i)
    delete.delete()
    return redirect(request.META['HTTP_REFERER'])


def del_To_do(request, i):
    delete = ToDoItem.objects.get(id=i)
    delete.delete()
    return redirect(request.META['HTTP_REFERER'])
