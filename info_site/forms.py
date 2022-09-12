from django import forms


class TextVisualizerForm(forms.Form):
    text = forms.CharField(label='Text to visualize: ')