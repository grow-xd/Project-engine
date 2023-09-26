from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import CustomUser
from project.models import Project
from project.serializers import ProjectSerializer

class ProfileView(APIView):
    def get(self, request, username, format=None):
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        projects = Project.objects.filter(created_by=user)
        serializer = ProjectSerializer(projects, many=True)

        profile_info = {
            'username': user.username,
            'name': user.name,
            'description': user.description,
            'projects_count': serializer.data
        }

        return Response(profile_info)
