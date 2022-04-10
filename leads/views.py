from django.core.mail import send_mail
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

class SigupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

class HomeView(TemplateView):
    template_name = "home.html"

class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/leads_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/leads_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(LoginRequiredMixin, CreateView):   
    template_name = "leads/leads_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

    # def form_valid(self, form):
    #     send_mail(
    #         subject="Bu lead yaratilingan",
    #         message="Yangi lead yarat",
    #         from_email="test@test.com",
    #         recipient_list=["test2@test.com"],
    #     )
    #     return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/leads_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/leads_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:lead-list")