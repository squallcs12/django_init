from rest_condition import And
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from common.rest.permissions import IsOwnerOrReadOnly


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name')


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (And(IsOwnerOrReadOnly, IsAuthenticated),)
    queryset = User.objects.exclude(is_staff=1)
    serializer_class = UserSerializer
