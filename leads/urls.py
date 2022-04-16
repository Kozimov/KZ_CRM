from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('<int:pk>/', LeadDetailView.as_view(), name='detallar'),
    path('<int:pk>/update_detail', LeadUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name="delete"),
    path('<int:pk>/agentni_aniqlash', AgentAssignView.as_view(), name="assign_agent"),
    path('create-leads/', LeadCreateView.as_view(), name="lead-create"),
    path('categories/', CategoryListView.as_view(), name="categories")
]