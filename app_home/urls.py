from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage, name="homepage"),
    # path('create/',views.create_post, name="create_post"),
    path('like/<str:post_id>/', views.like_post, name='like_post'),
    path('send-request/', views.send_friend_request, name="send_friend_request"),
    path('accept/<str:usr>/', views.accept_request, name="accept_req"),
    path('post/<str:p_id>/', views.view_one_post, name="view_one_post"),
    
    # Below are for only partial htmx request results.
    path('make_a_post/', views.make_a_post, name="make_a_post"),
    path('view_replies/<str:cmnt_uid>/', views.view_replies, name='view_replies'),
    path('create_comments/<str:post_uid>/', views.create_comments, name='create_comments'),
    path('create_reply/<str:cmnt_uid>/', views.create_reply, name='create_reply'),
    path('add_reply/', views.add_reply, name='add_reply'),
    path('search/', views.search, name='search'),
    
    path('temp/', views.temp, name="temp"),
    path('temp-p/', views.temp_partial, name="temp_partial"),


]
