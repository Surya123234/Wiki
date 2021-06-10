from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import newPageForm
from . import util
from django.urls import reverse
import random


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def display_entry(request, name):
    content = util.get_entry(name)
    if content is not None:
        return render(
            request,
            "encyclopedia/display_entry.html",
            {"name": name, "content": content},
        )
    return render(
        request, "encyclopedia/error.html", {"name": name, "try_to_save": False}
    )


def search(request):
    searched_entry = request.GET.get("q", "")
    matches = []

    for name in util.list_entries():
        # if the search matches an entry
        if searched_entry.casefold() == name.casefold():
            return redirect(reverse("encyclopedia:display_entry", args=[name]))
        # if the search is a substring of an entry
        if searched_entry.casefold() in name.casefold():
            matches.append(name)

    if len(matches) > 0:
        return render(
            request,
            "encyclopedia/matches.html",
            {"name": searched_entry, "matches": matches},
        )

    # if the search does not exist as an entry or a substring of an entry
    return render(
        request,
        "encyclopedia/error.html",
        {"name": searched_entry, "try_to_save": False},
    )


def new(request):
    if request.method == "POST":
        form = newPageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            content = form.cleaned_data["content"]

            # if the page already exists
            for entry in util.list_entries():
                if name.casefold() == entry.casefold():
                    return render(
                        request,
                        "encyclopedia/error.html",
                        {"name": name, "try_to_save": True},
                    )
            # if the page does NOT already exist
            util.save_entry(name, content)
            return redirect(reverse("encyclopedia:display_entry", args=[name]))
        else:
            return render(request, "encyclopedia/new.html", {"form": form})

    # if the request method was GET
    return render(request, "encyclopedia/new.html", {"form": newPageForm()})


def edit(request):
    return render(request, "encyclopedia/edit.html")


def random_page(request):
    name = random.choice(util.list_entries())
    return redirect(reverse("encyclopedia:display_entry", args=[name]))
