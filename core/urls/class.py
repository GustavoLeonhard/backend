from django.urls import path
from ..views import (
    ClassListView, ClassDetailView, ClassCreateView,
    ClassUpdateView, ClassDeleteView
)

app_name = 'class'

urlpatterns = [
    path('', ClassListView.as_view(), name='class_list'),
    path('<int:pk>/', ClassDetailView.as_view(), name='class_detail'),
    path('create/', ClassCreateView.as_view(), name='class_create'),
    path('<int:pk>/update/', ClassUpdateView.as_view(), name='class_update'),
    path('<int:pk>/delete/', ClassDeleteView.as_view(), name='class_delete'),
] 