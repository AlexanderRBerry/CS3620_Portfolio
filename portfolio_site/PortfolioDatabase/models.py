from django.db import models

# Create your models here.
class Hobby(models.Model):
    name = models.CharField(("Hobby Name"), max_length=50)
    description = models.TextField("Hobby Description")
    monthly_cost = models.DecimalField("Hobby Monthly cost", max_digits=10, decimal_places=2)
    image = models.ImageField("Hobby Image", upload_to="hobbies/", blank=True, null=True)

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"
        ordering = ["name"]

    def __str__(self):
        return self.name
class Portfolio(models.Model):
    name = models.CharField(("Portfolio Name"), max_length=50)
    description = models.TextField("Portfolio Description")
    #blank=True allows forms to accept blank fields
    #null=True allows the null in the database
    portfolio_link = models.URLField(("Portfolio Link"), max_length=200, blank=True, null=True)
    image = models.ImageField("Portfolio Image", upload_to="portfolios/", blank=True, null=True)

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
        ordering = ["name"]

    def __str__(self):
        return self.name