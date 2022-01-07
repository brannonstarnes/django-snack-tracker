from django.views.generic import TemplateView, ListView, DetailView

from django.views.generic import TemplateView, DetailView, ListView
from snacks.models import Snack

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

class AboutPageView(TemplateView):
    template_name= "about.html"

class HomePageView(TemplateView):
    template_name = "home.html"