from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import random
from django import forms
from . import util


class newPageForm(forms.Form):
    title = forms.CharField(label="title", max_length=100)
    content = forms.CharField(widget=forms.Textarea, label="content")

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
    else:
        return HttpResponseRedirect(reverse("wiki:dispMessage", kwargs={"message": "Page does not exist"}))

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
        form = newPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("wiki:viePageRequest", kwargs={"title":title}))
        else:   
            return HttpResponseRedirect(reverse("wiki:dispMessage", kwargs={"message": "Entry not Valid"}))
    
    if request.method=="GET":
        content = util.get_entry(title)
        if content != None:
            form1 = newPageForm(initial={
                'title':title,
                'content':content
                })
            return render(request, "encyclopedia/editPage.html", {
                "form": form1,
                "title": title
            })
        else:
            return HttpResponseRedirect(reverse("wiki:dispMessage", kwargs={"message": "Page does not exist"}))

def delPage(request, title):
    util.deletePage(title)
    return HttpResponseRedirect(reverse("wiki:index"))        


def randomPage(request):
    entryList = util.list_entries()
    randomPage = random.choice(entryList)
    return HttpResponseRedirect(reverse("wiki:viePageRequest", kwargs={'title': randomPage}))


def dispMessage(request, message):
    return render(request, "encyclopedia/message.html", {
            "message" : message
    })