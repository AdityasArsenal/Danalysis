def extractor(req_kpis, df, column_A_list, column_A_set):
    
    my_strings = req_kpis

    matches = []

    KPIs = []
    Periods = []
    Units = []
    Decimals = []
    Values = []


    for s in my_strings:                            # iterate over the required KPIs
        if s in column_A_set:
            index = column_A_list.index(s)
            matches.append((index))

    print("Matches found at:", matches)

    for match in matches:
        row = df.iloc[match]                        # get the row of the match
        
        kpi = row['Element Name']
        KPIs.append(kpi)

        period = row['Period'] 
        Periods.append(period)

        unit = row['Unit']
        Units.append(unit)

        decimal = row['Decimals']
        Decimals.append(decimal)

        value = row['Fact Value']
        Values.append(value)

        print()

    return KPIs, Periods, Units, Decimals, Values