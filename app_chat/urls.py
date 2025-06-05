from django.urls import path, re_path
from . import views, consumers

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    # path('messages/with/<str:u_id>/', views.messages, name='messages'),    
    path("<slug:room_name>/", views.chat_room, name="messages"),
]
