import requests
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from rates.models import CurrencyRequest

class CurrencyService:
    API_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    
    @classmethod
    def can_make_request(cls) -> bool:
        last_request = CurrencyRequest.objects.order_by('-created_at').first()
        
        if not last_request:
            return True
        
        now = timezone.now()
        time_diff = now - last_request.created_at
        
        return time_diff >= timedelta(seconds=10)
    
    @classmethod
    def fetch_and_save_usd_rate(cls) -> Decimal:
        response = requests.get(cls.API_URL)
        response.raise_for_status()
        
        data = response.json()
        
        usd_rate = Decimal(str(data['Valute']['USD']['Value']))
        
        CurrencyRequest.objects.create(ticker='USD', rate=usd_rate)
        
        return usd_rate
    
    @classmethod
    def get_history(cls, limit: int = 10):
        return CurrencyRequest.objects.order_by('-created_at')[:limit]