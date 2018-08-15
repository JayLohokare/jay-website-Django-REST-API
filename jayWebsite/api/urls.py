from django.conf.urls import url, include
from rest_framework import routers
from jayWebsite.api import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'education', views.EducationiewSet)
router.register(r'experience', views.ExperienceViewSet)
router.register(r'awards', views.AwardsViewSet)
router.register(r'research', views.ResearchViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^projects/', include('rest_framework.urls', namespace='projects')),
    url(r'^education/', include('rest_framework.urls', namespace='education')),
    url(r'^experience/', include('rest_framework.urls', namespace='experience')),
    url(r'^awards/', include('rest_framework.urls', namespace='awards')),
    url(r'^research/', include('rest_framework.urls', namespace='research'))
]