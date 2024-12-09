from django.shortcuts import render
from .models import StockDetails
import requests
from django.http import JsonResponse

def first(request):
    return render(request , 'first.html')

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,'signup.html')

def success(request):
    return render(request,'signupsuccess.html')

def dash(request):
    return render(request , 'dashboard.html')

def sigview(request):
    stockes = StockDetails.objects.all()
    return render(request, 'signal-view.html', {'stockes': stockes})

def stockview(request):
    return render(request,'stockscreener.html')

def fetch_filtered_data(request):
    # Replace this with your stock market API endpoint and key
    api_url = f"https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?apikey={api_key}"
    api_key = 'bc1SXQFdHuNkiU79vEEnPfktcSSxXGph'

    # Get user-selected filters from the request
    stock_exchange = request.GET.get('stock_exchange', '')
    sector = request.GET.get('sector', '')
    price_range = request.GET.get('price_range', '')

    # Call the API and fetch data
    response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})
    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch data from API'}, status=500)
    
    data = response.json()

    # Filter the data based on user selections
    filtered_data = []
    for stock in data:
        if stock_exchange and stock['exchange'] != stock_exchange:
            continue
        if sector and stock['sector'] != sector:
            continue
        if price_range:
            min_price, max_price = map(float, price_range.replace('$', '').split('-'))
            if not (min_price <= stock['price'] <= max_price):
                continue
        filtered_data.append(stock)

    return JsonResponse({'stocks': filtered_data}, status=200)







