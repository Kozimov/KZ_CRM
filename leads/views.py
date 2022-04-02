
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import models
from .forms import *


def leads_lists(request):
    leads = models.Lead.objects.all()
    context = {
        "leads": leads,
    }
    return render(request, "leads_lists.html", context)


def lead_detail(request, pk):
    lead = get_object_or_404(models.Lead, id=pk)
    context = {
        "lead": lead
    }
    return render(request, 'details.html', context)

def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            ismi = form.cleaned_data['ismi']
            familiyasi = form.cleaned_data['familiyasi']
            yoshi = form.cleaned_data['yoshi']
            agent = models.Agent.objects.first()
            models.Lead.objects.create(
                ismi=ismi,
                familiyasi=familiyasi,
                yoshi=yoshi,
                agent=agent
            )
            return redirect("/leads")
    context = {
        "forms": form
    }
    return render(request, "create.html", context)