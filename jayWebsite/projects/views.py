from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all() #.order_by('-date_joined')
    serializer_class = ProjectSerializer

