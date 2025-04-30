from django.urls import path
from ..views.institution import (
    InstitutionListView, InstitutionDetailView,
    InstitutionCreateView, InstitutionUpdateView,
    InstitutionDeleteView
)

app_name = 'institutions'

urlpatterns = [
    path('', InstitutionListView.as_view(), name='list'),
    path('<int:pk>/', InstitutionDetailView.as_view(), name='detail'),
    path('create/', InstitutionCreateView.as_view(), name='create'),
    path('<int:pk>/update/', InstitutionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', InstitutionDeleteView.as_view(), name='delete'),
] 