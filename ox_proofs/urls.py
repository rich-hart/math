from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from api.views import (TheoremViewSet, 
                    AxiomViewSet,
                    AxiomHighlight, 
                    DefinitionViewSet,
                    UserViewSet,
                    GroupViewSet,
                    TheoremHighlight,
                    DefinitionHighlight,
                    ArgumentViewSet,
                    StatementViewSet,
                    BookViewSet,)

from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework import renderers, response, schemas

from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()

router.register(r'users',UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'arguments',ArgumentViewSet)
router.register(r'statements',StatementViewSet)


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='OKR API')
    return response.Response(generator.get_schema(request=request))

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^$', schema_view),
    url(r'^api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


