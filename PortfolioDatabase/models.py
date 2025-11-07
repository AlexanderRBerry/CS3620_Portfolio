from django.db import models

# Create your models here.
class Hobby(models.Model):
    name = models.CharField(("Hobby Name"), max_length=50)
    description = models.TextField("Hobby Description")
    monthly_cost = models.DecimalField("Hobby Monthly cost", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class HobbyImage(models.Model):
    hobby = models.ForeignKey(
        Hobby,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="hobbies/")
    alt_text = models.CharField(max_length=150, blank=True)
    order = models.PositiveIntegerField(default=2)
    class meta:
        ordering = ["order", "id"]
    def __str__(self):
        return f"{self.hobby} {self.id}"
    
class Portfolio(models.Model):
    name = models.CharField(("Portfolio Name"), max_length=50)
    description = models.TextField("Portfolio Description")
    #blank=True allows forms to accept blank fields
    #null=True allows the null in the database
    portfolio_link = models.URLField(("Portfolio Link"), max_length=200, blank=True, null=True)
    # The image field is going to be replaced by an image model with a foreign key to this model
    #image = models.ImageField("Portfolio Image", upload_to="portfolios/", blank=True, null=True)

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="portfolios/")
    alt_text = models.CharField(max_length=150, blank=True)
    order = models.PositiveSmallIntegerField(default=2)

    class Meta:
        ordering = ["order", "id"]
    def __str__(self):
        return f"{self.portfolio} {self.id}"