from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models


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
    return render(request, "create.html")