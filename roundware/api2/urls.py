# Roundware Server is released under the GNU Lesser General Public License.
# See COPYRIGHT.txt, AUTHORS.txt, and LICENSE.txt in the project root directory.


from __future__ import unicode_literals
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from roundware.api2 import views
import logging
logger = logging.getLogger(__name__)


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'assets', views.AssetViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'listenevents', views.ListenEventViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'sessions', views.SessionViewSet)
router.register(r'stream', views.StreamViewSet, base_name="Stream")
router.register(r'tags', views.TagViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^obtain_token/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
)
