from django.conf.urls import url, include
from rest_framework import routers
from jayWebsite.projects import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^projects/', include('rest_framework.urls', namespace='projects'))
]