from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.addPage, name="addNewPage"),
    path("<str:title>", views.viewPageReq, name="viePageRequest"),
]
