from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from hierarchical_app.models import Tree
from hierarchical_app.forms import AddTreeForm, LoginForm


@login_required
def index_view(request):
    return render(request, "index.html", {'tree': Tree.objects.all()})


def add_tree_view(request):
    if request.method == "POST":
        form = AddTreeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tree.objects.create(
                name = data.get("name"),
                parent = data.get("parent"),
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddTreeForm()
    return render(request, "generic_form.html", {"form": form})


def tree_detail(request, tree_id):
    my_tree = Tree.objects.filter(id=tree_id).first()
    return render(request, "tree_detail.html", {})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))