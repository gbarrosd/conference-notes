from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import F
from decimal import Decimal

from .models import Notes, Items, Observation
from .forms import formNotes, FormItems, addObservation

@login_required
def dashboard(request):
    notes = Notes.objects.all()
    context = {
        'notes': notes
    }

    return render(request, 'core/dashboard.html', context)

@login_required
def storeNote(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['creator_user'] = request.user.id
        form = formNotes(data)
        if form.is_valid():
            note = form.save()
    
            return redirect('note.detail', note.id)
        context = {
            'form':form,
        }
        return render(request, 'core/storeNotes.html', context)
    else:
        form = formNotes()
        context = {
            'form':form,
        }
        return render(request, 'core/storeNotes.html', context)

@login_required
def detail(request, id):
    note = Notes.objects.filter(pk=id).first()
    items = Items.objects.filter(note=id)
    observations = Observation.objects.filter(note=id)
    context = {
        'note': note,
        'items':items,
        'observations':observations
    }
    return render(request, 'core/detailNote.html', context)

@login_required
def updateNote(request, id):
    note = get_object_or_404(Notes, pk=id)
    form = formNotes(instance=note)
    if request.method == 'POST':
        form = formNotes(request.POST, instance=note)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('note.detail', args=[id]))
    else:
        context = {
            'form':form,
            'idNote':id,
        }
        return render(request, 'core/updateNote.html', context)

@login_required
def deleteNote(request, id):
    note = get_object_or_404(Notes, pk=id)
    note.delete()

    return redirect('dashboard')

@login_required
def storeItem(request, id):
    if request.method == 'POST':
        data = request.POST.copy()
        data['note'] = id
        incrementValue = float(data['value'])
        form = FormItems(data)
        if form.is_valid():
            form.save()
            Notes.objects.filter(pk=id).update(total_value=F('total_value')+incrementValue)
        return HttpResponseRedirect(reverse('note.detail', args=[id]))
    else:
        form = FormItems()
        context = {
            'form':form,
            'idNote':id
        }
        return render(request, 'core/storeItem.html', context)

@login_required
def updateItem(request, id):
    item = get_object_or_404(Items, pk=id)
    oldItemValue = item.value
    form = FormItems(instance=item)
    if request.method == 'POST':
        idNote = request.POST['idNote']
        form = FormItems(request.POST, instance=item)
        if form.is_valid():
            form.save()
            valueRequest = Decimal(request.POST['value'].replace(',','.'))
            if oldItemValue < valueRequest:
                increment = valueRequest - oldItemValue
                Notes.objects.filter(pk=idNote).update(total_value=F('total_value')+increment)
            if oldItemValue > valueRequest:
                increment = oldItemValue - valueRequest
                Notes.objects.filter(pk=idNote).update(total_value=F('total_value')-increment)
        return HttpResponseRedirect(reverse('note.detail', args=[idNote]))
    else:
        context = {
            'form':form,
            'idNote': item.note.id,
            'idItem': item.id
        }
        return render(request, 'core/updateItem.html', context)

@login_required
def deleteItem(request, id):
    item = get_object_or_404(Items, pk=id)
    noteId = item.note.id
    oldValueItem = item.value
    item.delete()
    Notes.objects.filter(pk=noteId).update(total_value=F('total_value')-oldValueItem)
    return HttpResponseRedirect(reverse('note.detail', args=[noteId]))

@login_required
def storeObservation(request, id):
    if request.method == 'POST':
        data = request.POST.copy()
        data['note'] = id
        form = addObservation(data)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('note.detail', args=[id]))
    else:
        form = addObservation()
        context = {
            'form':form,
            'idNote':id,
        }

        return render(request, 'core/storeObservation.html', context)

@login_required
def deleteObservation(request, id):
    obs = get_object_or_404(Observation, pk=id)
    noteId = obs.note.id
    obs.delete()

    return HttpResponseRedirect(reverse('note.detail', args=[noteId]))

