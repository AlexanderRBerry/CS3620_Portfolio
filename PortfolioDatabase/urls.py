from django.contrib import admin
from django.urls import path
from . import views

app_name = "PortfolioDatabase"
urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies/', views.HobbyListView.as_view(), name="hobbies"),
    path('hobbies/<int:pk>/', views.HobbyDetailView.as_view(), name = "hobby_details"), 
    path('portfolio/', views.PortfolioListView.as_view(), name="portfolio"),
    path('portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name="portfolio_details"),
    path('contact/', views.contact, name="contact"),
]