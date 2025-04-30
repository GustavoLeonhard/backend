from django.urls import path
from ..views.institution import (
    InstitutionListView, InstitutionDetailView,
    InstitutionCreateView, InstitutionUpdateView,
    InstitutionDeleteView
)

urlpatterns = [
    path('', InstitutionListView.as_view(), name='institution_list'),
    path('<int:pk>/', InstitutionDetailView.as_view(), name='institution_detail'),
    path('create/', InstitutionCreateView.as_view(), name='institution_create'),
    path('<int:pk>/update/', InstitutionUpdateView.as_view(), name='institution_update'),
    path('<int:pk>/delete/', InstitutionDeleteView.as_view(), name='institution_delete'),
] 