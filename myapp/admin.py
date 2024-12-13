from django.contrib import admin # type: ignore
from .models import StockDetails
from .models import StockRecord
# Register your models here.


class StockDetailsAdmin(admin.ModelAdmin):
    list_display = ['stock_name', 'bought_below', 'sold_above', 'gain_percentage', 'signal_sent', 'signal_closed']
    search_fields = ['stock_name']

admin.site.register(StockDetails, StockDetailsAdmin)

class StockRecordAdmin(admin.ModelAdmin):
    list_display = ('TradDt', 'BizDt', 'Sgmt', 'Src', 'FinInstrmTp', 'FinInstrmId', 'TckrSymb', 'FinInstrmNm', 'OpnPric', 'ClsPric')
    search_fields = ('FinInstrmId', 'TckrSymb', 'FinInstrmNm')
    list_filter = ('Sgmt', 'Src', 'FinInstrmTp', 'BizDt')
    ordering = ('-TradDt',)

admin.site.register(StockRecord, StockRecordAdmin)



