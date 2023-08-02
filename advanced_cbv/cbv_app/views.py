from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView, 
                                  CreateView, DeleteView, UpdateView)

from django.urls import reverse_lazy
from . import models
# Create your views here.

class IndexView(TemplateView):
    template_name = 'cbv_app/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injected_content'] = "This is injected text from Class Based View..."
    #     return context

class SchoolListView(ListView):
    # context_object_name = 'school'    // You can define custom variable name to use it on view page...
    # Bydefault ListView return MODEL_NAME_list name to use it on view page for  for loop
    model = models.School

class SchoolDetailView(DetailView):
    #DetailView will return Bydefault variable name:  school ( means MODEL_NAME only )
    context_object_name = 'school_details'
    model = models.School
    template_name = 'cbv_app/school_details.html'

# create a view:
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolDeleteView(DeleteView):    
    model = models.School
    success_url = reverse_lazy('cbv_app:schoollist')










