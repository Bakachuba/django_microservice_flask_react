from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from mscore.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('products.api.urls'))
]

if DEBUG:
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    ] + debug_toolbar_urls()

# if not settings.TESTING:
#     urlpatterns = [
#         *urlpatterns,
#     ] + debug_toolbar_urls()