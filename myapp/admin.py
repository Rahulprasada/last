from django.contrib import admin
from .models import StockDetails
# Register your models here.


class StockDetailsAdmin(admin.ModelAdmin):
    list_display = ['stock_name', 'bought_below', 'sold_above', 'gain_percentage', 'signal_sent', 'signal_closed']
    search_fields = ['stock_name']

admin.site.register(StockDetails, StockDetailsAdmin)


