from django.urls import path

from . import views

app_name ="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/add", views.addPage, name="addNewPage"),
    path("wiki/edit", views.editPage, name="editPage"),
    path("wiki/del", views.delPage, name="delPage"),
    path("wiki/<str:title>", views.viewPageReq, name="viePageRequest"),
]
