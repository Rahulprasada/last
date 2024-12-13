from django.db import models  # type: ignore
from django.utils import timezone  # type: ignore

# Model to store stock alerts
class StockDetails(models.Model):
    stock_name = models.CharField(max_length=255)
    bought_below = models.DecimalField(max_digits=10, decimal_places=2)
    sold_above = models.DecimalField(max_digits=10, decimal_places=2)
    gain_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    signal_sent = models.DateTimeField(default=timezone.now)
    signal_closed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.stock_name

    class Meta:
        db_table = 'stock_details'

# Model to store stock market records
class StockRecord(models.Model):
    trad_dt = models.DateField(db_column='TradDt')
    biz_dt = models.DateField()
    sgmt = models.CharField(max_length=50)
    src = models.CharField(max_length=50)
    fin_instrm_tp = models.CharField(max_length=50)
    fin_instrm_id = models.CharField(max_length=50)
    isin = models.CharField(max_length=50)
    tckr_symb = models.CharField(max_length=50)
    scty_srs = models.CharField(max_length=50)
    xpry_dt = models.DateField(null=True, blank=True)
    fin_instrm_actl_xpry_dt = models.DateField(null=True, blank=True)
    strk_pric = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    optn_tp = models.CharField(max_length=50, null=True, blank=True)
    fin_instrm_nm = models.CharField(max_length=100)
    opn_pric = models.DecimalField(max_digits=10, decimal_places=2)
    hgh_pric = models.DecimalField(max_digits=10, decimal_places=2)
    lw_pric = models.DecimalField(max_digits=10, decimal_places=2)
    cls_pric = models.DecimalField(max_digits=10, decimal_places=2)
    last_pric = models.DecimalField(max_digits=10, decimal_places=2)
    prvs_clsg_pric = models.DecimalField(max_digits=10, decimal_places=2)
    undrlyg_pric = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sttlm_pric = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    opn_intrst = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    chng_in_opn_intrst = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ttl_tradg_vol = models.IntegerField(null=True, blank=True)
    ttl_trf_val = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ttl_nb_of_txs_exctd = models.IntegerField(null=True, blank=True)
    ssn_id = models.CharField(max_length=50, null=True, blank=True)
    new_brd_lot_qty = models.IntegerField(null=True, blank=True)
    rmks = models.CharField(max_length=500, null=True, blank=True)
    rsvd1 = models.CharField(max_length=50, null=True, blank=True)
    rsvd2 = models.CharField(max_length=50, null=True, blank=True)
    rsvd3 = models.CharField(max_length=50, null=True, blank=True)
    rsvd4 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.fin_instrm_id} - {self.fin_instrm_nm}"

    class Meta:
        db_table = 'stock_record'
