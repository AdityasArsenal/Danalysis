def adder(KPIs, Values, Referance_Unit,  Units, Periods, Decimals, Not_Found, rb,rs,name_of_sheet):
    j = 1

    rs[f'A{j}'].value = 'Name'
    rs[f'B{j}'].value = 'KPI'
    rs[f'C{j}'].value = 'Value'
    rs[f'D{j}'].value = 'Unit'
    rs[f'E{j}'].value = 'Period'
    rs[f'F{j}'].value = 'Decimal'
    rs[f'G{j}'].value = 'Referance_Unit'
    rs[f'H{j}'].value = 'Not_Found'

    n = len(KPIs)
    for i in range(n):

        rs[f'B{i+2}'].value = KPIs[i]
        rs[f'C{i+2}'].value = Values[i]
        rs[f'D{i+2}'].value = Referance_Unit[i]
        rs[f'E{i+2}'].value = Units[i]
        rs[f'F{i+2}'].value = Periods[i]
        rs[f'G{i+2}'].value = Decimals[i]
        #rs[f'H{i+2}'].value = Not_Found[i]

    rb.save(F"res.xlsx")

        