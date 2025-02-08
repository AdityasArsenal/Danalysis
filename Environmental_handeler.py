def get_env_data_from_xml(root, namespaces, env_kpi_names):

    # Environmental KPIs
    found_env_kpi_names = []
    found_env_referance_unit = []
    found_env_values = []
    found_env_unit_refs = []
    found_env_periods = []
    found_env_decimals = []
    not_found_env_kpi_names = []

    g = 0

    for kpi_name in env_kpi_names:
        g += 1
        
        print(f'{g}.{kpi_name}')

        elements = root.findall(f'.//in-capmkt:{kpi_name}', namespaces=namespaces)

        if elements:
            for element in elements:
                if element is not None:
                    contextRef = element.get('contextRef')
                    value = element.text
                    decimal = element.get('decimals')
                    unit_ref = element.get('unitRef')
                    period_element = root.find(f'.//xbrli:context[@id="{contextRef}"]/xbrli:period', namespaces=namespaces)
                    if period_element is not None:
                        startPeriod = period_element.find('xbrli:startDate', namespaces=namespaces)
                        endPeriod = period_element.find('xbrli:endDate', namespaces=namespaces)
                    else:
                        period = 'NA'

                    if "2023" in startPeriod.text:

                        if kpi_name == "AmountOfReUsed" or kpi_name == "AmountOfRecycled":                                                        #time perriod check
                            if contextRef == "D_PlasticsIncludingPackaging":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_env_kpi_names.append(extended_KPI_Name)
                                found_env_referance_unit.append(contextRef)
                                found_env_values.append(value)
                                found_env_decimals.append(decimal)
                                found_env_unit_refs.append(unit_ref)
                                found_env_periods.append(f"{startPeriod.text}--{endPeriod.text}")
                                print("---------------------------- \n")
                            elif contextRef == "D_EWaste":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_env_kpi_names.append(extended_KPI_Name)
                                found_env_referance_unit.append(contextRef)
                                found_env_values.append(value)
                                found_env_decimals.append(decimal)
                                found_env_unit_refs.append(unit_ref)
                                found_env_periods.append(f"{startPeriod.text}--{endPeriod.text}")
                                print("---------------------------- \n")
                            elif contextRef == "D_HazardousWaste":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_env_kpi_names.append(extended_KPI_Name)
                                found_env_referance_unit.append(contextRef)
                                found_env_values.append(value)
                                found_env_decimals.append(decimal)
                                found_env_unit_refs.append(unit_ref)
                                found_env_periods.append(f"{startPeriod.text}--{endPeriod.text}")
                                print("---------------------------- \n")
                            elif contextRef == "D_OtherWaste1":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_env_kpi_names.append(extended_KPI_Name)
                                found_env_referance_unit.append(contextRef)
                                found_env_values.append(value)
                                found_env_decimals.append(decimal)
                                found_env_unit_refs.append(unit_ref)
                                found_env_periods.append(f"{startPeriod.text}--{endPeriod.text}")
                                print("---------------------------- \n")

                        elif "Percentage" in kpi_name:
                            found_env_kpi_names.append(kpi_name)
                            found_env_referance_unit.append(contextRef)
                            found_env_values.append(f"{float(value)*100}%")
                            found_env_decimals.append(decimal)
                            found_env_unit_refs.append(unit_ref)
                            found_env_periods.append(f"{startPeriod.text}--{endPeriod.text}")
                            
                            print("---------------------------- \n")

                        else:
                            found_env_kpi_names.append(kpi_name)
                            found_env_referance_unit.append(contextRef)
                            found_env_values.append(value)
                            found_env_decimals.append(decimal)
                            found_env_unit_refs.append(unit_ref)
                            found_env_periods.append(f"{startPeriod.text}--{endPeriod.text}")
                            
                            print("---------------------------- \n")
        else:
            not_found_env_kpi_names.append(kpi_name)
            print(f"🔴Element not found for {kpi_name}\n")

    print(len(found_env_kpi_names))
    print(len(found_env_values))
    print(len(found_env_referance_unit))
    print(len(found_env_unit_refs))
    print(len(found_env_periods))
    print(len(found_env_decimals))
    print(len(not_found_env_kpi_names))

    return found_env_kpi_names, found_env_values, found_env_referance_unit, found_env_unit_refs, found_env_periods, found_env_decimals, not_found_env_kpi_names
