import csv
import pprint
with open('ExchangeRate.csv',encoding='utf-8',newline='') as file:
    csvReader = csv.reader(file)
    rates = list(csvReader)
pp = pprint.PrettyPrinter(
    indent=2,
    width=300,
    compact=True
)
pp.pprint(rates)