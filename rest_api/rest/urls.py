from django.urls import path

from .views import ProjectView

urlpatterns = [
    path('projects/', ProjectView.as_view(), name='projects'),
    path('projects/<int:id>', ProjectView.as_view(), name='projects_process')
]
