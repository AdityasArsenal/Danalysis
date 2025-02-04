import pandas as pd
from openpyxl import load_workbook
from extra_stuff.one_to_other_sheet.extract_data import extractor
from extra_stuff.one_to_other_sheet.add_data_to_sheet import adder

rb =load_workbook("exs/res.xlsx")  # Connect to the open file
rs = rb.active

df = pd.read_excel('exs/ee.xlsx', sheet_name='Intance Data')

column_A_list = list(df["Element Name"].astype(str))
column_A_set = set(column_A_list)

req_kpis = ['TotalScope1Emissions',
            'TotalWageCost', 
            'TotalWasteGenerated',
            'Greenhouse Gas (GHG) Emissions',
            'TotalScope1Emissions',
            'TotalScope2Emissions',
            'TotalScope3Emissions',
            'TotalScope3Emissions per rupee of turnover',
            'TotalScope1AndScope2EmissionsPerRupeeOfTurnover',
            'Waste Management',
            'Total Waste Generated',
            'Total Waste Disposed',
            'Landfilling',
            'Incineration',
            'E-waste',
            'Battery waste',
            'Plastic waste',
            'Bio-medical waste',
            'Radioactive waste',
            'Other Hazardous waste',
            'Construction and demolition waste',
            'Other Non-hazardous waste generated',
            'Waste Intensity per rupee of turnover',
            'Total waste recovered',
            'Re-used',
            'Recycled',
            'Water Management',
            'Total water withdrawal',
            'Water withdrawal from groundwater',
            'Water withdrawal from surface water',
            'Water withdrawal from third party water',
            'Water withdrawal from seawater/desalinated water',
            'Water withdrawal from other sources',
            'Total water consumption',
            'Total water discharged',
            'Total water discharged to groundwater (with treatment)',
            'Total water discharged to groundwater (without treatment)',
            'Total water discharged to surface water (with treatment)',
            'Total water discharged to surface water (without treatment)',
            'Total water discharged to seawater (with treatment)',
            'Total water discharged to seawater (without treatment)',
            'Total water discharged sent to third parties (with treatment)',
            'Total water discharged sent to third parties (without treatment)',
            'Total water discharged to others (with treatment)',
            'Total water discharged to others (without treatment)',
            'Total water recovered',
            'Water intensity per rupee of turnover',
            'Energy Management',
            'Total energy consumed',
            'Total energy consumed from renewable sources',
            'Total energy consumed from non-renewable sources',
            'Energy Intensity per rupee of turnover']

KPIs, Periods, Units, Decimals, Values = extractor(req_kpis, df, column_A_list, column_A_set)

adder(KPIs, Periods, Units, Decimals, Values,rb,rs)

