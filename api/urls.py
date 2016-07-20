from django.conf.urls import url, include
from rest_framework import routers
from .views import ProofViewSet 

router = routers.DefaultRouter()
router.register(r'proofs', ProofViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
