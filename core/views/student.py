from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from ..models import Student
from ..forms import StudentForm

class StudentListView(ListView):
    model = Student
    template_name = 'core/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'core/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('core:student_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('core:student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'core/student_confirm_delete.html'
    success_url = reverse_lazy('core:student_list') 