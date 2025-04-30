"""
Forms for the school administration system.

This module contains all the ModelForms used for creating and updating
institutions, teachers, students, classes, subjects, enrollments, and schedules.
"""

from django import forms
from .models import Institution, Teacher, Student, Class, Subject, Enrollment, Schedule

class InstitutionForm(forms.ModelForm):
    """Form for creating and updating institutions."""
    class Meta:
        model = Institution
        fields = ['name', 'address', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class TeacherForm(forms.ModelForm):
    """Form for creating and updating teachers."""
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'phone', 'institution', 'hire_date']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.Select(attrs={'class': 'form-control'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'address', 'phone', 'email', 'institution']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'institution': forms.Select(attrs={'class': 'form-control'}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['institution', 'grade', 'section', 'academic_year', 'class_teacher']
        widgets = {
            'institution': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2023-2024'}),
            'class_teacher': forms.Select(attrs={'class': 'form-control'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'description', 'institution']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'institution': forms.Select(attrs={'class': 'form-control'}),
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'class_instance', 'enrollment_date']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'class_instance': forms.Select(attrs={'class': 'form-control'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['class_instance', 'subject', 'teacher', 'day', 'start_time', 'end_time', 'room']
        widgets = {
            'class_instance': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'room': forms.TextInput(attrs={'class': 'form-control'}),
        } 