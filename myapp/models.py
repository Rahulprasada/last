from django.db import models # type: ignore
from django.utils import timezone # type: ignore

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
    


class StockRecord(models.Model):
    TradDt = models.DateField()
    BizDt = models.DateField()
    Sgmt = models.CharField(max_length=50)
    Src = models.CharField(max_length=50)
    FinInstrmTp = models.CharField(max_length=50)
    FinInstrmId = models.CharField(max_length=50)
    ISIN = models.CharField(max_length=50)
    TckrSymb = models.CharField(max_length=50)
    SctySrs = models.CharField(max_length=50)
    XpryDt = models.DateField(null=True, blank=True)
    FininstrmActlXpryDt = models.DateField(null=True, blank=True)
    StrkPric = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    OptnTp = models.CharField(max_length=50, null=True, blank=True)
    FinInstrmNm = models.CharField(max_length=100)
    OpnPric = models.DecimalField(max_digits=10, decimal_places=2)
    HghPric = models.DecimalField(max_digits=10, decimal_places=2)
    LwPric = models.DecimalField(max_digits=10, decimal_places=2)
    ClsPric = models.DecimalField(max_digits=10, decimal_places=2)
    LastPric = models.DecimalField(max_digits=10, decimal_places=2)
    PrvsClsgPric = models.DecimalField(max_digits=10, decimal_places=2)
    UndrlygPric = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    SttlmPric = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    OpnIntrst = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ChngInOpnIntrst = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    TtlTradgVol = models.IntegerField(null=True, blank=True)
    TtlTrfVal = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    TtlNbOfTxsExctd = models.IntegerField(null=True, blank=True)
    SsnId = models.CharField(max_length=50, null=True, blank=True)
    NewBrdLotQty = models.IntegerField(null=True, blank=True)
    Rmks = models.CharField(max_length=500, null=True, blank=True)
    Rsvd1 = models.CharField(max_length=50, null=True, blank=True)
    Rsvd2 = models.CharField(max_length=50, null=True, blank=True)
    Rsvd3 = models.CharField(max_length=50, null=True, blank=True)
    Rsvd4 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.FinInstrmId
