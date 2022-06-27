from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from requests.models import ProductRequest
from users.permissions import IsRequester
from ..serializers import ProductRequestEditSerializer


class PRRequesterViewset(ModelViewSet):
    permission_classes = (IsRequester,)
    authentication_classes = (JWTAuthentication,)

    def get_serializer_class(self):
        if self.action.lower() == 'list':
            pass
        return ProductRequestEditSerializer

    def get_queryset(self):
        user = self.request.user
        return ProductRequest.objects.filter(requester=user)
