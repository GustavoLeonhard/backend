from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Schedule
from ..forms import ScheduleForm

class ScheduleListView(ListView):
    model = Schedule
    template_name = 'core/schedule_list.html'
    context_object_name = 'schedules'

class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'core/schedule_detail.html'
    context_object_name = 'schedule'

class ScheduleCreateView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'core/schedule_form.html'
    success_url = reverse_lazy('core:schedule_list')

class ScheduleUpdateView(UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'core/schedule_form.html'
    success_url = reverse_lazy('core:schedule_list')

class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'core/schedule_confirm_delete.html'
    success_url = reverse_lazy('core:schedule_list') 