from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Project, Education, Experience, Research, Awards


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ResearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Research
        fields = '__all__'

class AwardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Awards
        fields = '__all__'
