from django.urls import path
from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.display_entry, name="display_entry"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit"),
    path("delete", views.delete, name="delete"),
    path("random", views.random_page, name="random_page"),
]
