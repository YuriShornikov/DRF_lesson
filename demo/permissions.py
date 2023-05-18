from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    # def has_permission(self, request, view):#имеет ли пользователь право на работу с ресами в целом
    def has_object_permission(self, request, view, obj):#имеет ли пользователь права на конкретные действия
        if request.method == 'GET':#прописываем методы, которые может использовать пользователь
            return True
        return request.user == obj.user#при совпадении права есть