from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm
from leads.models import Agent

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/list.html"

    def get_queryset(self):
        return Agent.objects.all()

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')


    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.profil = self.request.user.userprofil
        agent.save()
        return super(AgentCreateView, self).form_valid(form)