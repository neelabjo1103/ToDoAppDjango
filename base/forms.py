from django import forms

# Reordering Form and Viewx


class PositionForm(forms.Form):
    position = forms.CharField()
