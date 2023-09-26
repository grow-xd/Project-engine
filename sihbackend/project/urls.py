from django.urls import path
from .views import ProjectCreateView, ProjectListView, ProjectDetailView

urlpatterns = [
    path('projects/create/', ProjectCreateView.as_view(), name='create-project'),
    path('', ProjectListView.as_view(), name='list-projects'),
    path('<int:project_id>/', ProjectDetailView.as_view(), name='get-project'),
]
