from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)

class IsHR(permissions.BasePermission):
    def has_permission(self, request, view):
        logger.info(f'User: {request.user.username}, is_hr: {getattr(request.user, "is_hr", None)}, is_admin: {getattr(request.user, "is_admin", None)}')
        return (
            request.user
            and request.user.is_authenticated
            and (getattr(request.user, "is_hr", False) or getattr(request.user, "is_admin", False))
        )
