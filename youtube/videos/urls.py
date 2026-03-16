from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('<int:video_id>/', views.video_detail, name='video_detail'),
    path('upload/', views.video_upload_page, name='video_upload'),
    path('upload/submit/', views.video_upload, name='video_upload_submit'),
    path('channel/<str:username>/', views.channel_videos, name="channel"),
    path('<int:video_id>/delete/', views.video_delete, name="delete"),
    path('<int:video_id>/vote/', views.video_vote, name="vote")
]
