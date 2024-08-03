from django.urls import path
from .views import RegisterView, LoginView, CampaignListCreate, CampaignDetail, DonationListCreate, DonationDetail

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    
    path('campaigns/', CampaignListCreate.as_view(), name='campaign-list-create'),
    path('campaigns/<int:pk>/', CampaignDetail.as_view(), name='campaign-detail'),

    path('donations/', DonationListCreate.as_view(), name='donation-list-create'),
    path('donations/<int:pk>/', DonationDetail.as_view(), name='donation-detail'),
]
