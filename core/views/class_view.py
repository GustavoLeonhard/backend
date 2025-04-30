from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Class
from ..forms import ClassForm

class ClassListView(ListView):
    model = Class
    template_name = 'core/class_list.html'
    context_object_name = 'classes'

class ClassDetailView(DetailView):
    model = Class
    template_name = 'core/class_detail.html'
    context_object_name = 'class'

class ClassCreateView(CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'core/class_form.html'
    success_url = reverse_lazy('core:class_list')

class ClassUpdateView(UpdateView):
    model = Class
    form_class = ClassForm
    template_name = 'core/class_form.html'
    success_url = reverse_lazy('core:class_list')

class ClassDeleteView(DeleteView):
    model = Class
    template_name = 'core/class_confirm_delete.html'
    success_url = reverse_lazy('core:class_list') 