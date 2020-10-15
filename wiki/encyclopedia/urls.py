from django.urls import path

from . import views

app_name ="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/add", views.addPage, name="addNewPage"),
    path("wiki/edit/<str:title>", views.editPage, name="editPage"),
    path("wiki/del/<str:title>", views.delPage, name="delPage"),
    path("wiki/random", views.randomPage, name="randomPage"),
    path("wiki/message/<str:message>", views.dispMessage, name="dispMessage"),
    path("wiki/<str:title>", views.viewPageReq, name="viePageRequest"),
]
