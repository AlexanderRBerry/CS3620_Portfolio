from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby, Portfolio
# Create your views here.
def home(request):
    return render(request, "index.html")
def hobbies(request):
    hobby_queryset = Hobby.objects.all()
    return render(request, "hobbies.html", {"hobbies" : hobby_queryset})
def portfolio(request):
    portfolio_queryset = Portfolio.objects.all()
    return render(request, "portfolio.html", {"portfolios": portfolio_queryset})
def contact(request):
    return render(request, "contact.html")


# Example of rendering from a template
#def homepage(request):
#    entries = Entry.objects.order_by('-created_at')
#    return render(request, "index.html", {'entries': entries})