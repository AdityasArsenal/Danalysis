def extractor(j,ws,rs):
    i = 0
    value = True
    while value:
        i += 1
        print(i)
        if ws[f'B{i}'].value == "NameOfTheCompany":
            print(f"the name of the company is: {ws[f'F{i}'].value} ")

            rs[f'B{j}'].value = ws[f'F{i}'].value
            value = False

        elif ws[f'B{i}'].value == "CorporateIdentityNumber":
            print(f"the CorporateIdentityNumber value is: {ws[f'F{i}'].value}")

            rs[f'C{j}'].value = ws[f'F{i}'].value
            print()
            


