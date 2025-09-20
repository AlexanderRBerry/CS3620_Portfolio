from django.shortcuts import render
from .models import Hobby, Portfolio
from django.views.generic import ListView, DetailView
# Create your views here.
#def home(request):
#    return render(request, "index.html")
def home(request):
    featured = Portfolio.objects.order_by("id")[:3]  # last 3 for now
    featured = Portfolio.objects.filter(pk__in=[3, 6, 7])
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

class PortfolioListView(ListView):
    model = Portfolio
    template_name = "portfolio.html"
    context_object_name = "portfolios"
    paginate_by = 10
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio_details.html"
    context_object_name = "portfolio"

def contact(request):
    return render(request, "contact.html")
