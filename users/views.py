from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from .models import CustomUser
from .forms import formUser, UpdateUser, UpdateUserPassword

@login_required
def display(request):
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'users/listUsers.html', context)

@login_required
def store(request):
    if request.method == 'POST':
        form = formUser(request.POST)

        if form.is_valid():
            form.save()

            return redirect('list.users')

        form = formUser(request.POST)
        context = {
            'form': form
        }
        return render(request, 'users/addUser.html', context)

    else:
        form = formUser()
        context = {
            'form': form
        }
        return render(request, 'users/addUser.html', context)

@login_required
def detail(request, id):
    usr = CustomUser.objects.filter(pk=id).get()

    context = {
        'usr': usr
    }

    return render(request, 'users/detailUser.html', context)

@login_required
def update(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    form = UpdateUser(instance=user)
    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail.user', args=[id]))

        form = UpdateUser(request.POST)
        context = {
            'form': form
        }
        return render(request, 'users/updateUser.html', context)
    else:
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'users/updateUser.html', context)

@login_required
def delete(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    idUser = user.id

    user.delete()

    return redirect('list.users')