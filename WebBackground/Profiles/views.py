from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile

class ProfilesListView(ListView):
    model=Profile
    template_name="Profiles/profile_list.html"
    paginate_by=3

class ProfilesDetailView(DetailView):
    model=Profile
    template_name="Profiles/profile_Detail.html"
    
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
