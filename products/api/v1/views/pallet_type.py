from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.models import PalletType
from users.permissions import IsRequester
from ..serializers import PalletTypeSerializer


class PalletTypeListAPIView(ListAPIView):
    permission_classes = (IsRequester,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PalletTypeSerializer
    queryset = PalletType.objects.all()
