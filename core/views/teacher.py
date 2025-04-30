"""
Views for managing teachers in the school administration system.
"""
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models.teacher import Teacher
from ..forms import TeacherForm

class TeacherListView(ListView):
    """View for listing all teachers."""
    model = Teacher
    template_name = 'core/teacher_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    """View for displaying details of a specific teacher."""
    model = Teacher
    template_name = 'core/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherCreateView(CreateView):
    """View for creating a new teacher."""
    model = Teacher
    form_class = TeacherForm
    template_name = 'core/teacher_form.html'
    success_url = reverse_lazy('core:teacher_list')

class TeacherUpdateView(UpdateView):
    """View for updating an existing teacher."""
    model = Teacher
    form_class = TeacherForm
    template_name = 'core/teacher_form.html'
    success_url = reverse_lazy('core:teacher_list')

class TeacherDeleteView(DeleteView):
    """View for deleting a teacher."""
    model = Teacher
    template_name = 'core/teacher_confirm_delete.html'
    success_url = reverse_lazy('core:teacher_list') 