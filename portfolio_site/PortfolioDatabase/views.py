from django.shortcuts import render
from .models import Hobby, Portfolio
from django.views.generic import ListView, DetailView
# Create your views here.
#def home(request):
#    return render(request, "index.html")
def home(request):
    #featured = Portfolio.objects.order_by("id")[:3]  # Last 3 Projects
    featured = Portfolio.objects.filter(pk__in=[3, 6, 7]) # The specific projects I want to show off
    return render(request, "index.html", {"featured": featured})

class HobbyListView(ListView):
    model = Hobby
    template_name = "hobbies.html"
    context_object_name = "hobbies"
    paginate_by = 10
class HobbyDetailView(DetailView):
    model = Hobby
    template_name = "hobby_details.html"
    context_object_name = "hobby"
    def get_queryset(self): 
        return Hobby.objects.prefetch_related("images")

class PortfolioListView(ListView):
    model = Portfolio
    template_name = "portfolio.html"
    context_object_name = "portfolios"
    paginate_by = 10
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio_details.html"
    context_object_name = "portfolio"
    # This grabs all related images at once which is much more efficent and scalable
    def get_queryset(self): 
        return Portfolio.objects.prefetch_related("images")

def contact(request):
    return render(request, "contact.html")
