from django.db import models
from .institution import Institution
from .teacher import Teacher

class Class(models.Model):
    GRADE_CHOICES = [
        (1, '1st Grade'),
        (2, '2nd Grade'),
        (3, '3rd Grade'),
        (4, '4th Grade'),
        (5, '5th Grade'),
        (6, '6th Grade'),
        (7, '7th Grade'),
        (8, '8th Grade'),
        (9, '9th Grade'),
        (10, '10th Grade'),
        (11, '11th Grade'),
        (12, '12th Grade'),
    ]

    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
        ('D', 'Section D'),
    ]

    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='classes')
    grade = models.IntegerField(choices=GRADE_CHOICES)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    academic_year = models.CharField(max_length=9)  # Format: 2023-2024
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='managed_classes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Classes'
        unique_together = ['institution', 'grade', 'section', 'academic_year']

    def __str__(self):
        return f"{self.grade}{self.section} - {self.academic_year}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='subjects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Schedule(models.Model):
    DAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
    ]

    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='schedules')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='schedules')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='schedules')
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['class_instance', 'day', 'start_time']

    def __str__(self):
        return f"{self.subject} - {self.day} {self.start_time}-{self.end_time}" 