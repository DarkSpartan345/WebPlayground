from django.urls import path
from .views import ProfilesListView,ProfilesDetailView

Profiles_patterns=([path('',ProfilesListView.as_view(),name="ListView"),
             path('<username>/',ProfilesDetailView.as_view(),name="DetailView"),
             ],"profiles")