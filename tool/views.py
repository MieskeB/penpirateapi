import mimetypes
import zipfile

from django.http import HttpResponse
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


def generate(request):
    code = request.POST['code']
    cmdname = request.POST['name']

    commandfile = open('command', 'w')
    commandfile.write('#!/usr/bin/env python3\n\n' + code)
    makefile = open('makefile', 'w')
    makefile.write('all: environment rights command\n\nenvironment:\n	sed -i \'1s/^/#!\\/usr\\/bin\\/env python3\\n\\n/\' ./command\n\nrights:\n	chmod +x ./command\n\ncommand:\n	cp ./command /usr/bin/' + cmdname)

    export = zipfile.ZipFile('file.zip', 'w')
    export.write('command')
    export.write('makefile')

    download = open('file.zip', 'r')
    mime_type, _ = mimetypes.guess_type('file.zip')
    response = HttpResponse(download, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % 'file.zip'
    return response
