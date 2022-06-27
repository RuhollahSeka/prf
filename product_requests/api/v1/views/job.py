from rest_framework import mixins, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from product_requests.models import Job
from users.permissions import IsFulfiller
from ..serializers import JobEditSerializer


class JobViewSet(mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    permission_classes = (IsFulfiller,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = JobEditSerializer
    queryset = Job.objects.all()
