from django.db import models
from django.utils import timezone

# Create your models here.
class StockDetails(models.Model):
    stock_name = models.CharField(max_length=255)
    bought_below = models.DecimalField(max_digits=10, decimal_places=2)
    sold_above = models.DecimalField(max_digits=10, decimal_places=2)
    gain_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    signal_sent = models.DateTimeField(default=timezone.now)
    signal_closed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.stock_name
    

    

    