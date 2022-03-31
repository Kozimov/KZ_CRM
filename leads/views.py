from multiprocessing import context
from django.shortcuts import render
from . import models


def leads_lists(request):
    leads = models.Lead.objects.all()
    context = {
        "leads": leads,
    }
    return render(request, "leads_lists.html", context)