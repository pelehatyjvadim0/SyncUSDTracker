from django.http import JsonResponse
from rates.services import CurrencyService

# Create your views here.
def get_current_usd(request):
    if not CurrencyService.can_make_request():
        return JsonResponse(
            {'error': 'Too many requests. Please wait 10 seconds between requests.'},
            status = 429
        )
        
    try:
        current_rate = CurrencyService.fetch_and_save_usd_rate()
        
        history = CurrencyService.fetch_and_save_usd_rate()
        
        history = CurrencyService.get_history(limit=10)
        
        history_data = [
            {
                'rate': float(item.rate),
                'date': item.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            for item in history
        ]
        
        return JsonResponse({
            'current_usd_rate': float(current_rate),
            'last_10_requests': history_data
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 500)