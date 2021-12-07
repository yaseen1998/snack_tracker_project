from django.db.models import fields
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model=Snack
class HomeView(TemplateView):
    template_name = 'home.html'


class SnackDeatailView(DetailView):
    template_name = 'snack_detail.html'
    model=Snack
    # context_object_name = 'yaseen' # change name of model 

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['name','description','purchaser']

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['name','description','purchaser']
class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')