from django.shortcuts import render
from pathlib import Path
from . import forms
import logging

import spacy
from spacy import displacy


def index(request):
    return render(request, 'index.html')


def spacy_visualizer(request):
    displacy_opts = {
        'fine_grained': True,
        'compact': True,
    }

    if request.method == 'POST':
        form = forms.TextVisualizerForm(request.POST)

        if form.is_valid():
            nlp = spacy.load('es_dep_news_trf')

            # Tokenize the cleaned version of the entered text
            procd = nlp(form.cleaned_data['text'])
            # Generate SVG of dependency tree of the text
            procd_img = displacy.render(
                procd, style='dep', options=displacy_opts
            )

            procd_filename = 'procd-image.svg'
            procd_path = Path('./info_site/static/info_site/images/')
            (procd_path/procd_filename).open('w', encoding='utf-8').write(procd_img)

            context = {
                'form': form,
                'text_dep_img': f'info_site/images/{procd_filename}',
            }

            return render(
                request,
                'visualizer.html',
                context=context
            )

    else:
        text = 'Sample Spanish text goes here!'

        form = forms.TextVisualizerForm(
            initial={
                'text': text,
            }
        )

    return render(request, 'visualizer.html', context={'form': form})
