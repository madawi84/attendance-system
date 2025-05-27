from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)

class IsHR(permissions.BasePermission):
    def has_permission(self, request, view):
        logger.info(f'User: {request.user.username}, is_hr: {request.user.is_hr}')
        return request.user and request.user.is_authenticated and request.user.is_hr
