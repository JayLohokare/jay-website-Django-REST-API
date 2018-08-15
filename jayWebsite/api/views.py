from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import ProjectSerializer, EducationSerializer, ExperienceSerializer, ResearchSerializer, AwardsSerializer
from .models import Project, Education, Experience, Research, Awards


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('order')
    serializer_class = ProjectSerializer
    http_method_names = ['get']

class EducationiewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Education.objects.all().order_by('order')
    serializer_class = EducationSerializer
    http_method_names = ['get']

class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Experience.objects.all().order_by('order')
    serializer_class = ExperienceSerializer
    http_method_names = ['get']

class ResearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Research.objects.all().order_by('order')
    serializer_class = ResearchSerializer
    http_method_names = ['get']

class AwardsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Awards.objects.all().order_by('order')
    serializer_class = AwardsSerializer
    http_method_names = ['get']
