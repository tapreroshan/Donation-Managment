# donations/permissions.py
from rest_framework.permissions import BasePermission

class IsReceiver(BasePermission):
    def has_permission(self, request, view):
        return request.user.userprofile.user_type == 'receiver'

class IsDonor(BasePermission):
    def has_permission(self, request, view):
        return request.user.userprofile.user_type == 'donor'
