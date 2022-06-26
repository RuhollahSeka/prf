from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.api.v1.serializers import ShrinkWrapSerializer
from products.models import ShrinkWrap
from users.permissions import IsRequester


class ShrinkWrapListAPIView(ListAPIView):
    permission_classes = (IsRequester,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = ShrinkWrapSerializer
    queryset = ShrinkWrap.objects.all()
