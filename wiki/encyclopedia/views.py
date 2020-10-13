from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def viewPageReq(request, title):
    return render(request, "encyclopedia/viewPage.html", {
        "title": title,
        "content": util.get_entry(title)
    })

class newPageForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(label="content")

def addPage(request):
    if request.method=="POST":
        form = newPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if title.lower() in [entry.lower() for entry in util.list_entries()]:
                return render(request, "encyclopedia/pageExists.html", {
                    "form": form
                })
            else:
                util.save_entry(title, content)
            
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })        
        else:
            return render(request, "encyclopedia/addNewPage.html", {
                "form": form
            })

    return render(request, "encyclopedia/addNewPage.html", {
        "form": newPageForm()
    })