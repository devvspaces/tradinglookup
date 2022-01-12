import uuid
from django.db import models

# Create your models here.
class Ticker(models.Model):
    ticker = models.CharField(max_length=5)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default=None)
    market_cap = models.PositiveBigIntegerField()
    dividend = models.DecimalField(max_digits=3, decimal_places=2)
    ceo = models.CharField(max_length=30, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sector = models.ForeignKey('Sector', on_delete=models.CASCADE)
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE)
    employees = models.BigIntegerField(null=True)
    location = models.CharField(max_length=80, null=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
    primary_key=True, editable=False)



class Sector(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name