from django.db import models

# Create your models here.
class CurrencyRequest(models.Model):
    ticker = models.CharField(max_length=10, default='USD')
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.ticker}: {self.rate} at {self.created_at}'