from django import forms


class TextVisualizerForm(forms.Form):
    text = forms.CharField(label='Text to visualize: ')

    def clean_text(self):
        data = self.cleaned_data['text']

        return data