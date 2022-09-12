from django.shortcuts import render
from django.views.generic import View
from . import forms

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

            procd = nlp(form.cleaned_data['text'])
            procd_img = displacy.render(
                procd, style='dep', options=displacy_opts
            )

            context = {
                'text': form.cleaned_data['text'],
                'text_dep_img': procd_img,
            }

            return render(request, 'visualizer.html', {'form': forms.TextVisualizerForm(initial=context)})

    else:
        def_text = '@IsabelDK8 Hace unos días venía de estar varios días en Boquete, debo decir que al llegar a ese punto, la vista, la brisa, uno siente un gozo de contemplar la ciudad.'
        def_img = 'placeholder-no-bad-days.jpg'

        form = forms.TextVisualizerForm(
            initial={
                'text': def_text,
                'text_dep_img': def_img,
            }
        )

    context = {
        'form': form,
    }

    return render(request, 'visualizer.html', context)