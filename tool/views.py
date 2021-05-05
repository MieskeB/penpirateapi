from django.shortcuts import render, get_object_or_404

from .models import Tool


def index(request):
    tool = get_object_or_404(Tool, pk=1)
    files = tool.file_set.all()
    context = {
        'tool': tool,
        'files': files,
        'selectedFile': files[0]
    }
    return render(request, 'tool/index.html', context)
