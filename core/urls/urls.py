"""
URL patterns for the school administration system views.
"""
from django.urls import path
from ..views import (
    InstitutionListView, InstitutionCreateView, InstitutionUpdateView, InstitutionDeleteView,
    TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView,
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
)

app_name = 'core'

urlpatterns = [
    # Institution URLs
    path('institutions/', InstitutionListView.as_view(), name='institution_list'),
    path('institutions/create/', InstitutionCreateView.as_view(), name='institution_create'),
    path('institutions/<int:pk>/update/', InstitutionUpdateView.as_view(), name='institution_update'),
    path('institutions/<int:pk>/delete/', InstitutionDeleteView.as_view(), name='institution_delete'),

    # Teacher URLs
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),

    # Student URLs
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
] 