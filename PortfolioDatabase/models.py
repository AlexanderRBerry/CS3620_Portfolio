from django.db import models
from bs4 import BeautifulSoup, NavigableString
from django.utils.safestring import mark_safe

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
    #image = models.ImageField(upload_to="hobbies/")
    image_name = models.CharField(max_length=100, blank=True)
    alt_text = models.CharField(max_length=150, blank=True)
    order = models.PositiveIntegerField(default=2)
    def get_image_path(self):
        return f"images/hobbies/{self.image_name}"
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

    # for specifying potfolio order
    order = models.PositiveSmallIntegerField(default=2)

    # This method limits the length of the description (default 350 chars)
    # It also accepts html tags
    def short_description(self, char_limit=350):
        soup = BeautifulSoup(self.description, "html.parser")
        current_length = 0
        output = BeautifulSoup("", "html.parser")  # clean output soup

        def append_nodes(source, target):
            nonlocal current_length
            for element in source:
                if isinstance(element, NavigableString):
                    remaining = char_limit - current_length
                    text = str(element)
                    if remaining <= 0:
                        return False
                    if len(text) <= remaining:
                        target.append(text)
                        current_length += len(text)
                    else:
                        target.append(text[:remaining] + '...')
                        current_length = char_limit
                        return False
                else:
                    # Recursively preserve tags
                    new_tag = output.new_tag(element.name)
                    target.append(new_tag)
                    if not append_nodes(element.contents, new_tag):
                        return False
            return True

        append_nodes(soup.body.contents if soup.body else soup.contents, output)

        return mark_safe(str(output))


    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name
    
class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name="images"
    )
    #image = models.ImageField(upload_to="portfolios/")
    image_name = models.CharField(max_length=100, blank=True)
    alt_text = models.CharField(max_length=150, blank=True)
    order = models.PositiveSmallIntegerField(default=2)
    def get_image_path(self):
        return f"images/portfolios/{self.image_name}"
    
    class Meta:
        ordering = ["order", "id"]
    def __str__(self):
        return f"{self.portfolio} {self.id}"