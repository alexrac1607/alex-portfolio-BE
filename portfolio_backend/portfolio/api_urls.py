from django.urls import path
from .views import ProjectList, ProjectDetail, PostList, PostDetail

urlpatterns = [
    path('projects/', ProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]
