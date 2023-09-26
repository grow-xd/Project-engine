from django.urls import path
from .views import ProjectSearchView

urlpatterns = [
    path('search/', ProjectSearchView.as_view(), name='project-search'),
]
