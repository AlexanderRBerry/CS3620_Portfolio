from django.contrib import admin
from .models import Hobby, Portfolio, PortfolioImage, HobbyImage
# Register your models here.
class HobbyImageInline(admin.TabularInline):
    model = HobbyImage
    extra = 1
    fields = ("image_name", "alt_text", "order")
    ordering = ("order", "id")

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "monthly_cost")
    search_fields = ("name",)
    list_filter = ("monthly_cost",)
    ordering = ("name",)
    inlines = [HobbyImageInline]

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1
    fields = ("image_name", "alt_text", "order")
    ordering = ("order", "id")

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "portfolio_link", "has_link")
    search_fields = ("name",)
    # Filter by portfolios by those that have or do not have links
    list_filter = (("portfolio_link", admin.EmptyFieldListFilter),) 
    ordering = ("name",)
    inlines = [PortfolioImageInline]

    def has_link(self, obj):
        return bool(obj.portfolio_link)
    
