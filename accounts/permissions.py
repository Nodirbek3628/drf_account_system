from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = "siz Admin emassz"

    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class IsManager(BasePermission):
    message = "Siz Manager emassz"

    def has_permission(self, request, view):
        return request.user and request.user.is_manager
    
class IsUser(BasePermission):
    message = "siz Admin emassz"

    def has_permission(self, request, view):
        return request.user and request.user.is_user
    
class IsRoles(BasePermission):
    message = "Siz Manager emassz"

    def has_permission(self, request, view):
        return request.user and request.user.is_roles
    
class IsStaff(BasePermission):
    message = "Siz Manager emassz"

    def has_permission(self, request, view):
        return request.user and not [ request.user.is_roles or  request.user.is_user]