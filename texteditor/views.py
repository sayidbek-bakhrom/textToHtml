from django.shortcuts import render
from .forms import EditorForm


def index(request):
    form = EditorForm()
    context = {
        'form': form
    }
    return render(request, 'texteditor/index.html', context)


