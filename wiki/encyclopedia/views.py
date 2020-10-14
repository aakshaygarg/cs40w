from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django import forms
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def viewPageReq(request, title):
    content= util.get_entry(title)
    if content != None:
        content= util.convertToHTML(content)
    return render(request, "encyclopedia/viewPage.html", {
        "title": title,
        "content": content
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

            if title.lower() in [existingTitle.lower() for existingTitle in util.list_entries()]:
                return render(request, "encyclopedia/addNewPage.html", {
                    "errorMessage": f"Page With Title: {title} - Already Exists",
                    "form": form
                })
            else:
                util.save_entry(title, content)
            
            return HttpResponseRedirect(reverse("wiki:index"))        
        else:
            return render(request, "encyclopedia/addNewPage.html", {
                "errorMessage": "Form not Valid",
                "form": form
            })

    return render(request, "encyclopedia/addNewPage.html", {
        "errorMessage": "none",
        "form": newPageForm()
    })

def editPage(request, title):
    if request.method=="POST":
        content= util.get_entry(title)
        if content != None:
            form=newPageForm()
            form.title=title
            form.content=content
            return render(request, "encyclopedia/addNewPage.html", {
                "form": form
            })



def delPage(request):
    if True:
        return 1