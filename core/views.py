from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Institution, Teacher, Student, Class, Subject, Enrollment, Schedule
from .forms import (
    InstitutionForm, TeacherForm, StudentForm, ClassForm,
    SubjectForm, EnrollmentForm, ScheduleForm
)

# Create your views here.

def home(request):
    context = {
        'institution_count': Institution.objects.count(),
        'teacher_count': Teacher.objects.count(),
        'student_count': Student.objects.count(),
        'class_count': Class.objects.count(),
    }
    return render(request, 'core/home.html', context)

# Institution Views
class InstitutionListView(ListView):
    model = Institution
    template_name = 'core/institution_list.html'
    context_object_name = 'institutions'

class InstitutionDetailView(DetailView):
    model = Institution
    template_name = 'core/institution_detail.html'
    context_object_name = 'institution'

class InstitutionCreateView(CreateView):
    model = Institution
    form_class = InstitutionForm
    template_name = 'core/institution_form.html'
    success_url = reverse_lazy('core:institution_list')

class InstitutionUpdateView(UpdateView):
    model = Institution
    form_class = InstitutionForm
    template_name = 'core/institution_form.html'
    success_url = reverse_lazy('core:institution_list')

class InstitutionDeleteView(DeleteView):
    model = Institution
    template_name = 'core/institution_confirm_delete.html'
    success_url = reverse_lazy('core:institution_list')

# Teacher Views
class TeacherListView(ListView):
    model = Teacher
    template_name = 'core/teacher_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'core/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'core/teacher_form.html'
    success_url = reverse_lazy('core:teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'core/teacher_form.html'
    success_url = reverse_lazy('core:teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'core/teacher_confirm_delete.html'
    success_url = reverse_lazy('core:teacher_list')

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'core/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'core/student_detail.html'

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

# Class Views
class ClassListView(ListView):
    model = Class
    template_name = 'core/class_list.html'
    context_object_name = 'classes'

class ClassDetailView(DetailView):
    model = Class
    template_name = 'core/class_detail.html'

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

# Subject Views
class SubjectListView(ListView):
    model = Subject
    template_name = 'core/subject_list.html'
    context_object_name = 'subjects'

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'core/subject_detail.html'

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

# Enrollment Views
class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'core/enrollment_list.html'
    context_object_name = 'enrollments'

class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = 'core/enrollment_detail.html'

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

# Schedule Views
class ScheduleListView(ListView):
    model = Schedule
    template_name = 'core/schedule_list.html'
    context_object_name = 'schedules'

class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'core/schedule_detail.html'

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
