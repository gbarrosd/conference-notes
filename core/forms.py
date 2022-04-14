from django import forms

from .models import (
    Notes,
    Items,
    Observation,
)

class formNotes(forms.ModelForm):

    class Meta:
        model = Notes
        fields = (
            'vehicle_model',
            'plate',
            'creator_user',
        )
        widgets = {'creator_user': forms.HiddenInput()}

class FormItems(forms.ModelForm):

    class Meta:
        model = Items
        fields = (
            'description',
            'value',
            'note',
        )
        widgets = {'note': forms.HiddenInput()}

class addObservation(forms.ModelForm):

    class Meta:
        model = Observation
        fields = (
            'observation',
            'note'
        )
        widgets = {'note': forms.HiddenInput()}