from django.urls import path, re_path
from frontend.forum import views

urlpatterns = [
    # Home route.
    path('forum/', views.BoardListView.as_view(), name='forum'),

    # Boards route.
    re_path(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),

    # New post route.
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),

    # Topic view route.
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$',
            views.PostListView.as_view(),
            name='topic_posts'
            ),

    # Reply view route.
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$',
            views.reply_topic,
            name='reply_topic'
            ),

    # Post edit view route.
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
            views.PostUpdateView.as_view(),
            name='edit_post'
            ),
]
