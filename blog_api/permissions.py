from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Только аутентифицированные пользователи могут видеть представление списка
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение разрешено для любого запроса, поэтому мы всегда будем
        # разрешать запросы GET, HEAD или OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Права на запись разрешены только автору сообщения или администратору
        return obj.author == request.user or request.user.is_staff
