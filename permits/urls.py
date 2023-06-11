from django.urls import path
from .views import LongTermPermitListCreateView, LongTermPermitDetailView, LongTermWorkPermitApprovalView

urlpatterns = [
    path('long-term-permits/', LongTermPermitListCreateView.as_view(), name='longtermpermit-list'),
    path('long-term-permits/<int:pk>/', LongTermPermitDetailView.as_view(), name='longtermpermit-detail'),
    path('long-term-permits/<path:permit_number>/approval/', LongTermWorkPermitApprovalView.as_view(), name='longtermpermit-approval'),
]