from unicodedata import name
from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', ListsView.as_view()),
    path('<int:pk>/', LeadDetailView.as_view(), name='detallar'),
    path('<int:pk>/update_detail', lead_update, name='update'),
    path('<int:pk>/delete', lead_delete, name="delete"),
    path('create-leads/', lead_create, name="lead-create"),
]