"""
Views for the school administration system.
"""
from django.views.generic import TemplateView
from ..models import Institution, Teacher
from .institution import InstitutionListView, InstitutionDetailView, InstitutionCreateView, InstitutionUpdateView, InstitutionDeleteView
from .teacher import TeacherListView, TeacherDetailView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView
from .student import StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView
from .class_view import ClassListView, ClassDetailView, ClassCreateView, ClassUpdateView, ClassDeleteView
from .subject import SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView
from .enrollment import EnrollmentListView, EnrollmentDetailView, EnrollmentCreateView, EnrollmentUpdateView, EnrollmentDeleteView
from .schedule import ScheduleListView, ScheduleDetailView, ScheduleCreateView, ScheduleUpdateView, ScheduleDeleteView
from .home import HomeView

__all__ = [
    'HomeView',
    'InstitutionListView', 'InstitutionDetailView', 'InstitutionCreateView', 'InstitutionUpdateView', 'InstitutionDeleteView',
    'TeacherListView', 'TeacherDetailView', 'TeacherCreateView', 'TeacherUpdateView', 'TeacherDeleteView',
    'StudentListView', 'StudentDetailView', 'StudentCreateView', 'StudentUpdateView', 'StudentDeleteView',
    'ClassListView', 'ClassDetailView', 'ClassCreateView', 'ClassUpdateView', 'ClassDeleteView',
    'SubjectListView', 'SubjectDetailView', 'SubjectCreateView', 'SubjectUpdateView', 'SubjectDeleteView',
    'EnrollmentListView', 'EnrollmentDetailView', 'EnrollmentCreateView', 'EnrollmentUpdateView', 'EnrollmentDeleteView',
    'ScheduleListView', 'ScheduleDetailView', 'ScheduleCreateView', 'ScheduleUpdateView', 'ScheduleDeleteView'
] 