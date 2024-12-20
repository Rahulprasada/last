# Generated by Django 5.1.4 on 2024-12-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_stockrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockrecord',
            name='ChngInOpnIntrst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='FininstrmActlXpryDt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='NewBrdLotQty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='OpnIntrst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='OptnTp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='Rmks',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='Rsvd1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='Rsvd2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='Rsvd3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='Rsvd4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='SsnId',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='StrkPric',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='SttlmPric',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='TtlNbOfTxsExctd',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='TtlTradgVol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='TtlTrfVal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='UndrlygPric',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='XpryDt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='ClsPric',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='FinInstrmId',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='FinInstrmNm',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='FinInstrmTp',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='HghPric',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='ISIN',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='LastPric',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='LwPric',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='OpnPric',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='PrvsClsgPric',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='SctySrs',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='Sgmt',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='Src',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='TckrSymb',
            field=models.CharField(max_length=50),
        ),
    ]
