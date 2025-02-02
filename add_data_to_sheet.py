def adder(KPIs, Periods, Units, Decimals, Values,rb,rs):
    j = 1

    rs[f'A{j}'].value = 'Name'
    rs[f'B{j}'].value = 'KPI'
    rs[f'C{j}'].value = 'Value'
    rs[f'D{j}'].value = 'Unit'
    rs[f'E{j}'].value = 'Period'
    rs[f'F{j}'].value = 'Decimal'

    n = len(KPIs)

    for i in range(n):

        rs[f'B{i+2}'].value = KPIs[i]
        rs[f'C{i+2}'].value = Values[i]
        rs[f'D{i+2}'].value = Units[i]
        rs[f'E{i+2}'].value = Periods[i]
        rs[f'F{i+2}'].value = Decimals[i]

    rb.save("exs/res.xlsx")

        