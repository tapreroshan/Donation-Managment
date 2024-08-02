"""
URL configuration for Donation_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# charity_donation/urls.py
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from donation2.views import RegisterView, LoginView, PostListCreate, PostDetail, DonationListCreate, DonationDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/posts/', PostListCreate.as_view(), name='list_create_posts'),
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('api/donations/', DonationListCreate.as_view(), name='list_create_donations'),
    path('api/donations/<int:pk>/', DonationDetail.as_view(), name='donation_detail'),
]
