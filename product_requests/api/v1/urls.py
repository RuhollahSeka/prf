from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    prefix='requesters',
    viewset=views.RequesterPRViewset,
    basename='requester-requests',
)


urlpatterns = [

]

urlpatterns += router.urls
