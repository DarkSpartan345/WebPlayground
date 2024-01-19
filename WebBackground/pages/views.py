from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import PageForm
from django.shortcuts import redirect

class StaffRequiredMixin(object):
    #clase para verificar que cuando se modifique el CRUD lo haga alguien del staff
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs):
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)
    
class PagesListView(ListView):
    model=Page
class PageDetailView(DetailView):
    model=Page
class PageCreateView(StaffRequiredMixin,CreateView):
    model=Page
    form_class=PageForm
    success_url=reverse_lazy('pages:pages')
class PageUpdateView(StaffRequiredMixin,UpdateView):
    model=Page
    form_class=PageForm
    template_name_suffix='_update_form'
    def get_success_url(self):
        return reverse_lazy('pages:update',args=[self.object.id])+'?ok'
class PageDeleteView(StaffRequiredMixin,DeleteView):
    model=Page
    success_url=reverse_lazy('pages:pages')