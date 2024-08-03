from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Campaign, Donation, Transaction
from .serializers import UserSerializer, CampaignSerializer, DonationSerializer, TransactionSerializer

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

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

