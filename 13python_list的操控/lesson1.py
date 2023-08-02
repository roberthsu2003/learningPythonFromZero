import csv
import pprint
with open('ExchangeRate.csv',encoding='utf-8',newline='') as file:
    csvReader = csv.reader(file)
    rates = list(csvReader)
pp = pprint.PrettyPrinter(
    indent=1,
    width=200
)
pp.pprint(rates)