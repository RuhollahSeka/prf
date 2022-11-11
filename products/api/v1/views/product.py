# from rest_framework.filters import SearchFilter
# from rest_framework.generics import ListAPIView
# from rest_framework.pagination import PageNumberPagination
# from rest_framework_simplejwt.authentication import JWTAuthentication
#
# from products.models import Variant
# from users.permissions import IsRequester
# from ..serializers import VariantSerializer
#
#
# class VariantListAPIView(ListAPIView):
#     permission_classes = (IsRequester,)
#     authentication_classes = (JWTAuthentication,)
#     serializer_class = VariantSerializer
#     filter_backends = (SearchFilter,)
#     search_fields = ('code',)
#     queryset = Variant.objects.all()
#     pagination_class = PageNumberPagination
from elasticsearch_dsl import Q
from elasticsearch_dsl.query import Bool, Match
from rest_framework.response import Response
from rest_framework.views import APIView

from products.documents import VariantDocument


class VariantListAPIView(APIView):
    http_method_names = ('get',)

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')
        es_query = f'*{query}*'
        results = VariantDocument.search().query(Q(
            'bool',
            should=[Q('wildcard', name=es_query), Q('wildcard', code=es_query)]
        ))
        data = []
        for result in results:
            data.append({
                'name': result.name,
                'code': result.code,
            })
        return Response(data=data)
