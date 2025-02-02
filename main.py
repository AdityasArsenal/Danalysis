import pandas as pd
from openpyxl import load_workbook
from extract_data import extractor
from add_data_to_sheet import adder

rb =load_workbook("exs/res.xlsx")  # Connect to the open file
rs = rb.active

matches = [1,3,5]

df = pd.read_excel('exs/ee.xlsx', sheet_name='Intance Data')

column_A_list = list(df["Element Name"].astype(str))
column_A_set = set(column_A_list)

req_kpis = ['TotalScope1Emissions', 'TotalWageCost', 'TotalWasteGenerated']

KPIs, Periods, Units, Decimals, Values = extractor(req_kpis, df, column_A_list, column_A_set)

adder(KPIs, Periods, Units, Decimals, Values,rb,rs)

