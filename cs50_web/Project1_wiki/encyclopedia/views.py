from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, entryName):
    return render(request, "encyclopedia/entry.html", {
        "entryName": entryName,
        "entryField": util.get_entry(entryName), 
    })