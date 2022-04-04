from unicodedata import name
from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', leads_lists),
    path('<int:pk>/detallar', lead_detail, name='detallar'),
    path('<int:pk>/update_detail', lead_update, name='lead-update'),
    path('<int:pk>/delete', lead_delete, name="lead-delete"),
    path('create-yaratish/', lead_create, name="lead-create"),
]