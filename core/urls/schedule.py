from django.urls import path
from ..views import (
    ScheduleListView, ScheduleDetailView, ScheduleCreateView,
    ScheduleUpdateView, ScheduleDeleteView
)

app_name = 'schedule'

urlpatterns = [
    path('', ScheduleListView.as_view(), name='schedule_list'),
    path('<int:pk>/', ScheduleDetailView.as_view(), name='schedule_detail'),
    path('create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path('<int:pk>/update/', ScheduleUpdateView.as_view(), name='schedule_update'),
    path('<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),
] 