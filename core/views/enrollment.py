from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Enrollment
from ..forms import EnrollmentForm

class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'core/enrollment_list.html'
    context_object_name = 'enrollments'

class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = 'core/enrollment_detail.html'
    context_object_name = 'enrollment'

class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'core/enrollment_form.html'
    success_url = reverse_lazy('core:enrollment_list')

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'core/enrollment_form.html'
    success_url = reverse_lazy('core:enrollment_list')

class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'core/enrollment_confirm_delete.html'
    success_url = reverse_lazy('core:enrollment_list') 