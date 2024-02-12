from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import settings
from django.conf.urls.static import static

from graphene_django.views import GraphQLView

from users.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),

    # This is the URL for the GraphQL endpoint
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
