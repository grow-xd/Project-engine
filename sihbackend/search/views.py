from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from project.models import Project  # Import the Project model from your project app

class ProjectSearchView(APIView):
    def get(self, request, format=None):
        search_query = request.GET.get('q', '')  # Get the search query parameter from the URL
        projects = Project.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(languages_used__name__icontains=search_query)
        ).distinct()

        # Serialize the search results
        data = [{'id': project.id,'name': project.name, 'description': project.description, 'languages_used': [lang.name for lang in project.languages_used.all()]} for project in projects]

        return Response(data)
