import csv
from django.core.management.base import BaseCommand # type: ignore
from myapp.models import StockRecord 

class Command(BaseCommand):
    help = 'Import data from a CSV file into the database'

    def handle(self, *args, **kwargs):
        # Define the path to your CSV file
        file_path = r'C:\Users\Admin\Desktop\recovery\Miststreet\myapp\media\csv_files\excel_files.csv'
        
        # Open the CSV file
        with open(file_path, mode='r', encoding='utf-8') as file:
            # Use the CSV reader to read the file
            csv_reader = csv.DictReader(file)
            
            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Create a new StockRecord object for each row
                stock_record = StockRecord(
                    TradDt=row['TradDt'], 
                    BizDt=row['BizDt'],
                    Sgmt=row['Sgmt'],
                    Src=row['Src'],
                    FinInstrmTp=row['FinInstrmTp'],
                    FinInstrmId=row['FinInstrmId'],
                    ISIN=row['ISIN'],
                    TckrSymb=row['TckrSymb'],
                    SctySrs=row['SctySrs'],
                    XpryDt=row['XpryDt'] if row['XpryDt'] else None,
                    FininstrmActlXpryDt=row['FininstrmActlXpryDt'] if row['FininstrmActlXpryDt'] else None,
                    StrkPric=row['StrkPric'] if row['StrkPric'] else None,
                    OptnTp=row['OptnTp'],
                    FinInstrmNm=row['FinInstrmNm'],
                    OpnPric=row['OpnPric'],
                    HghPric=row['HghPric'],
                    LwPric=row['LwPric'],
                    ClsPric=row['ClsPric'],
                    LastPric=row['LastPric'],
                    PrvsClsgPric=row['PrvsClsgPric'],
                    UndrlygPric=row['UndrlygPric'] if row['UndrlygPric'] else None,
                    SttlmPric=row['SttlmPric'] if row['SttlmPric'] else None,
                    OpnIntrst=row['OpnIntrst'] if row['OpnIntrst'] else None,
                    ChngInOpnIntrst=row['ChngInOpnIntrst'] if row['ChngInOpnIntrst'] else None,
                    TtlTradgVol=row['TtlTradgVol'] if row['TtlTradgVol'] else None,
                    TtlTrfVal=row['TtlTrfVal'] if row['TtlTrfVal'] else None,
                    TtlNbOfTxsExctd=row['TtlNbOfTxsExctd'] if row['TtlNbOfTxsExctd'] else None,
                    SsnId=row['SsnId'],
                    NewBrdLotQty=row['NewBrdLotQty'] if row['NewBrdLotQty'] else None,
                    Rmks=row['Rmks'],
                    Rsvd1=row['Rsvd1'],
                    Rsvd2=row['Rsvd2'],
                    Rsvd3=row['Rsvd3'],
                    Rsvd4=row['Rsvd4']
                )

                # Save the record in the database
                stock_record.save()

        # Inform the user that the import is complete
        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV file'))
