from rest_framework import viewsets, generics, permissions

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

    def perform_create(self,serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)


class IsActiveEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                employee = User.objects.get(user=request.user)
                return employee.is_active
            except User.DoesNotExist:
                return False
        return False