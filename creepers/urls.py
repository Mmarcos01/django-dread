from django.urls import path
from .views import CreeperListView, CreeperDetailView, CreeperCreateView, CreeperUpdateView, CreeperDeleteView

urlpatterns = [
    path('', CreeperListView.as_view(), name='creeper_list'),
    path('<int:pk>/', CreeperDetailView.as_view(), name='creeper_detail'),
    path('create/', CreeperCreateView.as_view(), name='creeper_create'),
    path('<int:pk>/update/', CreeperUpdateView.as_view(), name='creeper_update'),
    path('<int:pk>/delete/', CreeperDeleteView.as_view(), name='creeper_delete'),
]
