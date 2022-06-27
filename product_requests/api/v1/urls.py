from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    prefix='requesters',
    viewset=views.RequesterPRViewset,
    basename='requester-requests',
)

router.register(
    prefix='fulfillers',
    viewset=views.FulfillerPRViewset,
    basename='fulfiller-requests',
)

router.register(
    prefix='jobs',
    viewset=views.JobViewSet,
    basename='jobs-edit',
)


urlpatterns = [

]

urlpatterns += router.urls
