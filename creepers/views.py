from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Creeper

class CreeperListView(ListView):
    template_name = "creeper/creeper-list.html"
    model = Creeper


class CreeperDetailView(DetailView):
    template_name = "creeper/creeper-detail.html"
    model = Creeper


class CreeperCreateView(CreateView):
    template_name = "creeper/creeper-create.html"
    model = Creeper
    fields = ['name', 'description', 'survivability', 'added']


class CreeperUpdateView(UpdateView):
    template_name = "creeper/creeper-update.html"
    model = Creeper
    fields = ['name', 'description', 'survivability',  'added']


class CreeperDeleteView(DeleteView):
    template_name = "creeper/creeper-delete.html"
    model = Creeper
    success_url = reverse_lazy("creeper_list")
