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
