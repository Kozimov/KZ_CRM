from django.urls import path
from .views import *

app_name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name="agent-list"),
    path('create-agents/', AgentCreateView.as_view(), name="agent-create"),
]