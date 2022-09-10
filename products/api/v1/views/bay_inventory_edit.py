from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from products.models import Variant, Bay, BayInventory
from ..serializers import BayInventoryEditSerializer


class BayInventoryEditAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BayInventoryEditSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._product_code = None
        self._bay_code = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self._product_code = request.data['product_code']
        self._bay_code = request.data['bay_code']

    def get_object(self):
        variant = Variant.objects.get(code=self._product_code)
        bay = Bay.objects.get(code=self._bay_code)
        bay_inventory = BayInventory.objects.get_or_create(
            variant=variant,
            bay=bay,
        )
        return bay_inventory
