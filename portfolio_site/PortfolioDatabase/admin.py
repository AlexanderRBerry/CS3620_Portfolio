from django.contrib import admin
from .models import Hobby, Portfolio
# Register your models here.
@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "monthly_cost")
    search_fields = ("name",)
    list_filter = ("monthly_cost",)
    ordering = ("name",)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "portfolio_link", "has_link")
    search_fields = ("name",)
    # Filter by portfolios by those that have or do not have links
    list_filter = (("portfolio_link", admin.EmptyFieldListFilter),) 
    ordering = ("name",)

    def has_link(self, obj):
        return bool(obj.portfolio_link)