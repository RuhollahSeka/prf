from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    prefix='requesters',
    viewset=views.PRRequesterViewset,
    basename='requester-requests',
)


urlpatterns = [

]

urlpatterns += router.urls
