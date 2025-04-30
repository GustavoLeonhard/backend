from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Subject
from ..forms import SubjectForm

class SubjectListView(ListView):
    model = Subject
    template_name = 'core/subject_list.html'
    context_object_name = 'subjects'

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'core/subject_detail.html'
    context_object_name = 'subject'

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'core/subject_form.html'
    success_url = reverse_lazy('core:subject_list')

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'core/subject_form.html'
    success_url = reverse_lazy('core:subject_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'core/subject_confirm_delete.html'
    success_url = reverse_lazy('core:subject_list') 