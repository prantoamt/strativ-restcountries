from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import Country
from api.utils.content_object import Content
# Create your views here.


class CountryListView(SuccessMessageMixin, LoginRequiredMixin, generic.ListView):
    model = Country
    contect_object_name = "country_list"
    template_name = "country/country_list.html"
    # paginate_by = 10

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        query = self.request.GET.get('name', None)
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Country List"
        return context


class CountryDetailView(SuccessMessageMixin, LoginRequiredMixin, generic.DetailView):
    model = Country
    template_name = "country/country_detail.html"
    # paginate_by = 10

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Country Details"
        object_id = self.kwargs['pk']
        content = Content()
        content.set_neighbour_countries_and_their_languages(object_id)
        context['details'] = content.get_data()
        return context
