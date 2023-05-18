from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from demo.models import Avs
from demo.permissions import IsOwnerOrReadOnly
from demo.serializers import AvsSerializer


# Create your views here.


class AvsViewSet(ModelViewSet):
    queryset = Avs.objects.all()
    serializer_class = AvsSerializer
    permission_classes = [IsOwnerOrReadOnly]#запрос без токена
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]#класс для подтверждения пользователя через токен
    #любой пользователь должен быть аутенфицирован и быть владельцем
    throttle_classes = [AnonRateThrottle]#включение тротлинга для анонимных пользователей


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
