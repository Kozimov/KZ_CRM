
from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from . import models
from .forms import *


class HomeView(TemplateView):
    template_name = "home.html"


class ListsView(ListView):
    template_name = "leads_lists.html"
    queryset = models.Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(DetailView):
    template_name = "details.html"
    queryset = models.Lead.objects.all()
    context_object_name = "lead"


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "forms": form
    }
    return render(request, "create.html", context)

def lead_update(request, pk):
    lead = models.Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        'lead': lead
    }
    return render(request, "update.html", context)

def lead_delete(request, pk):
    lead = models.Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

