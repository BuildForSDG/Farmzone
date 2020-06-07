from django.urls import path, re_path
from frontend.forum import views

urlpatterns = [
    path('forum/', views.ForumListView.as_view(), name='forum'),
    path('forum/<int:pk>/', views.TopicListView.as_view(), name='forum_topics'),
    path('forum/<int:pk>/new', views.new_topic, name='new_topic'),
    path('forum/<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('forum/<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    re_path(r'^forum/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
            views.PostUpdateView.as_view(), name='edit_post'),
]
