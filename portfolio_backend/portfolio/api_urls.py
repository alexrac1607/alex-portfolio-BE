from django.urls import path
from .views import ProjectList, ProjectDetail, PostList, PostDetail, RegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Project endpoints
    path('projects/', ProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project_detail'),

    # Post endpoints
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),

    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/user/', UserDetailView.as_view(), name='user_detail'),
]
