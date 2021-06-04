from django.http.response import HttpResponse
from django.shortcuts import render

from . import util


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
    return render(request, "encyclopedia/error.html", {"name": name})


def search(request):
    searched_entry = request.GET.get("q", "")
    matches = []

    for name in util.list_entries():
        # if the search matches an entry
        if searched_entry.casefold() == name.casefold():
            return render(
                request,
                "encyclopedia/display_entry.html",
                {"name": name, "content": util.get_entry(name)},
            )
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
    return render(request, "encyclopedia/error.html", {"name": searched_entry})
