from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Campaign, Donation, Transaction
from .serializers import UserSerializer, CampaignSerializer, DonationSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'message' : 'Signup Sucessful', 'userdetail': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': "Invalid Credential"}, status=status.HTTP_406_NOT_ACCEPTABLE)

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is not None:
            refresh = RefreshToken.for_user(user)
            response = Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            response.set_cookie(
            'refresh_token', str(refresh),
            httponly=True,
            secure=False
            )
            response.set_cookie(
                'access_token', str(refresh.access_token),
                httponly=True,
                secure=False
            )
            return response
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CampaignListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        campaigns = Campaign.objects.all()
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CampaignDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            campaign = Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            campaign = Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CampaignSerializer(campaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            campaign = Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DonationListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DonationDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            donation = Donation.objects.get(pk=pk)
        except Donation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DonationSerializer(donation)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            donation = Donation.objects.get(pk=pk)
        except Donation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DonationSerializer(donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            donation = Donation.objects.get(pk=pk)
        except Donation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)