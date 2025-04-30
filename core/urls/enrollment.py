from django.urls import path
from ..views import (
    EnrollmentListView, EnrollmentDetailView, EnrollmentCreateView,
    EnrollmentUpdateView, EnrollmentDeleteView
)

app_name = 'enrollment'

urlpatterns = [
    path('', EnrollmentListView.as_view(), name='enrollment_list'),
    path('<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('create/', EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('<int:pk>/update/', EnrollmentUpdateView.as_view(), name='enrollment_update'),
    path('<int:pk>/delete/', EnrollmentDeleteView.as_view(), name='enrollment_delete'),
] 