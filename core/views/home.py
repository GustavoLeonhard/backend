from django.views.generic import TemplateView
from ..models import Institution, Teacher, Student, Class, Subject, Enrollment, Schedule

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institution_count'] = Institution.objects.count()
        context['teacher_count'] = Teacher.objects.count()
        context['student_count'] = Student.objects.count()
        context['class_count'] = Class.objects.count()
        context['subject_count'] = Subject.objects.count()
        context['enrollment_count'] = Enrollment.objects.count()
        context['schedule_count'] = Schedule.objects.count()
        return context 