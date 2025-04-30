"""
URL patterns for the school administration system.
"""
from django.urls import path
from ..views import (
    HomeView,
    TeacherListView, TeacherDetailView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView,
    InstitutionListView, InstitutionDetailView, InstitutionCreateView, InstitutionUpdateView, InstitutionDeleteView,
    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    ClassListView, ClassDetailView, ClassCreateView, ClassUpdateView, ClassDeleteView,
    SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView,
    EnrollmentListView, EnrollmentDetailView, EnrollmentCreateView, EnrollmentUpdateView, EnrollmentDeleteView,
    ScheduleListView, ScheduleDetailView, ScheduleCreateView, ScheduleUpdateView, ScheduleDeleteView
)

app_name = 'core'

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),
    
    # Teachers
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),
    
    # Institutions
    path('institutions/', InstitutionListView.as_view(), name='institution_list'),
    path('institutions/<int:pk>/', InstitutionDetailView.as_view(), name='institution_detail'),
    path('institutions/create/', InstitutionCreateView.as_view(), name='institution_create'),
    path('institutions/<int:pk>/update/', InstitutionUpdateView.as_view(), name='institution_update'),
    path('institutions/<int:pk>/delete/', InstitutionDeleteView.as_view(), name='institution_delete'),
    
    # Students
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    
    # Classes
    path('classes/', ClassListView.as_view(), name='class_list'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class_detail'),
    path('classes/create/', ClassCreateView.as_view(), name='class_create'),
    path('classes/<int:pk>/update/', ClassUpdateView.as_view(), name='class_update'),
    path('classes/<int:pk>/delete/', ClassDeleteView.as_view(), name='class_delete'),
    
    # Subjects
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subjects/create/', SubjectCreateView.as_view(), name='subject_create'),
    path('subjects/<int:pk>/update/', SubjectUpdateView.as_view(), name='subject_update'),
    path('subjects/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
    
    # Enrollments
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('enrollments/create/', EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('enrollments/<int:pk>/update/', EnrollmentUpdateView.as_view(), name='enrollment_update'),
    path('enrollments/<int:pk>/delete/', EnrollmentDeleteView.as_view(), name='enrollment_delete'),
    
    # Schedules
    path('schedules/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedules/<int:pk>/', ScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedules/create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedules/<int:pk>/update/', ScheduleUpdateView.as_view(), name='schedule_update'),
    path('schedules/<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),
] 