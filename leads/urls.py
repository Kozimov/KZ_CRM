from unicodedata import name
from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', leads_lists),
    path('<int:pk>/', lead_detail, name='detallar'),
    path('<int:pk>/update_detail', lead_update, name='update'),
    path('<int:pk>/delete', lead_delete, name="delete"),
    path('create-leads/', lead_create, name="create"),
]