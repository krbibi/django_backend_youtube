from django.urls import path
from . import views
from reactions.views import ReactionAPIView

urlpatterns = [
    path('', views.VideoList.as_view(), name='video-list'),
    path('<int:pk>/', views.VideoDetail.as_view(), name='video-detail'), # api/v1/videos/<int:pk>
    # api/v1/video/{video_id}/reaction
    path('<int:video_id>/reaction',ReactionAPIView.as_view(), name='video-reaction')
]