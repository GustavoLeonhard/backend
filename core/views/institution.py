"""
Views for managing institutions in the school administration system.
"""
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models.institution import Institution
from ..forms import InstitutionForm

class InstitutionListView(ListView):
    """View for listing all institutions."""
    model = Institution
    template_name = 'core/institution_list.html'
    context_object_name = 'institutions'

class InstitutionDetailView(DetailView):
    """View for displaying details of a specific institution."""
    model = Institution
    template_name = 'core/institution_detail.html'
    context_object_name = 'institution'

class InstitutionCreateView(CreateView):
    """View for creating a new institution."""
    model = Institution
    form_class = InstitutionForm
    template_name = 'core/institution_form.html'
    success_url = reverse_lazy('core:institution_list')

class InstitutionUpdateView(UpdateView):
    """View for updating an existing institution."""
    model = Institution
    form_class = InstitutionForm
    template_name = 'core/institution_form.html'
    success_url = reverse_lazy('core:institution_list')

class InstitutionDeleteView(DeleteView):
    """View for deleting an institution."""
    model = Institution
    template_name = 'core/institution_confirm_delete.html'
    success_url = reverse_lazy('core:institution_list') 