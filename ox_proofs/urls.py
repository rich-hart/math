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
                    StatementViewSet,)


from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework import renderers, response, schemas

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

router.register(r'users',UserViewSet)
#router.register(r'groups',GroupViewSet)
router.register(r'arguments',ArgumentViewSet)
router.register(r'statements',StatementViewSet)
#router.register(r'definitionS', DefinitionViewSet)
#router.register(r'theorems', TheoremViewSet)
#router.register(r'axioms', AxiomViewSet)


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Pastebin API')
    return response.Response(generator.get_schema(request=request))

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url('^$', schema_view),

#    url(r'^definitionS/(?P<pk>[0-9]+)/highlight/$',DefinitionHighlight.as_view(),name='definition-highlight'),
#    url(r'^axioms/(?P<pk>[0-9]+)/highlight/$',AxiomHighlight.as_view(),name='axiom-highlight'),
#    url(r'^theorems/(?P<pk>[0-9]+)/highlight/$',TheoremHighlight.as_view(),name='theorem-highlight'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


