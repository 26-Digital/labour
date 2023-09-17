from django.urls import path
from .views import OmangCreateView, OmangViewSet, OmangListCreateView, OmangRetrieveUpdateDestroyView
from . import views

urlpatterns = [
    path('omang/create/', OmangCreateView.as_view(), name='create_omang'),
    path('omangs/', OmangListCreateView.as_view(), name='omang-list-create'),
    path('omang/<str:ID_Number>/', OmangRetrieveUpdateDestroyView.as_view(), name='omang-retrieve-update-destroy'),
    path('success/',views.success_view, name="success_page"),
    path('', views.home, name='home'),
]