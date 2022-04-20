from django.views.generic import ListView
from miapp.models import MiembroFlia

class FamiliaListView(ListView):
    model = MiembroFlia
    context_object_name = 'miembros'





    
