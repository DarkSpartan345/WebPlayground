from django.urls import path
from .views import ThreadListView,ThreadDetailView,add_message,start_thread

Messenger_patterns=([path('',ThreadListView.as_view(),name="ListView"),
             path('thread/<int:pk>/',ThreadDetailView.as_view(),name="DetailView"),
             path('thread/<int:pk>/add',add_message,name="add"),
             path('thread/start/<username>',start_thread,name="start"),
             ],"messenger")