from rest_framework import permissions

class IsAuthorReadOnly(permissions.BasePermission):
    # 모든 요청에 대해 허가
    def has_permission(self, request, view):
        return True
    # 작성자에 한해 삭제 허용
    def has_object_permission(self, request, views, obj):
        # 조회 요청은 항상 True
        if request.method in permissions.SAFE_METHODS:
            return True
        # PUT, DELETE 요청에 한해, 작성자에게만 허용
        return obj.author == request.user