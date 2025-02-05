def get_gov_data_from_xml(root, namespaces, env_kpi_names):

    # Governance KPIs
    found_gov_kpi_names = []
    found_gov_referance_unit = []
    found_gov_values = []
    found_gov_unit_refs = []
    found_gov_periods = []
    found_gov_decimals = []
    not_found_gov_kpi_names = []

    Total_NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages = 0
    Total_NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages = 0
    Total_NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages = 0
    Total_NumberOfWorkersForRemunerationOrSalaryOrWages = 0

    g = 0

    for kpi_name in env_kpi_names:
        g += 1
        print(f'{g}.')

        elements = root.findall(f'.//in-capmkt:{kpi_name}', namespaces=namespaces)

        if elements:

            if len(elements) == 3:
                if kpi_name == "NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages":
                    
                    if contextRef == "D_Male_p5":
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages+= int(value)

                    elif contextRef == "D_Female_p5":
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages+= int(value)
                        
                    else:
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages+= int(value)
                        
                elif kpi_name == "NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages":
                    
                    if contextRef == "D_Male_p5":
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages+= int(value)

                    elif contextRef == "D_Female_p5":
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages+= int(value)
                        
                    else:
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages+= int(value)

                elif kpi_name == "NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages":
                    
                    if contextRef == "D_Male_p5":
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages+= int(value)

                    elif contextRef == "D_Female_p5":
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages+= int(value)
                        
                    else:
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages+= int(value)

                elif kpi_name == "NumberOfWorkersForRemunerationOrSalaryOrWages":
                    
                    if contextRef == "D_Male_p5":
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfWorkersForRemunerationOrSalaryOrWages+= int(value)

                    elif contextRef == "D_Female_p5":
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfWorkersForRemunerationOrSalaryOrWages+= int(value)
                        
                    else:
                        extended_kpi_name = f"{kpi_name}--{contextRef}"
                        found_gov_kpi_names.append(extended_kpi_name)
                        found_gov_referance_unit.append(contextRef)
                        found_gov_values.append(value)
                        found_gov_decimals.append(decimal)
                        found_gov_unit_refs.append(unit_ref)
                        found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")

                        Total_NumberOfWorkersForRemunerationOrSalaryOrWages+= int(value)
                        print("========================\n")

            else:
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
                            found_gov_kpi_names.append(kpi_name)
                            found_gov_referance_unit.append(contextRef)
                            found_gov_values.append(value)
                            found_gov_decimals.append(decimal)
                            found_gov_unit_refs.append(unit_ref)
                            found_gov_periods.append(f"{startPeriod.text}--{endPeriod.text}")
                            
                            print("---------------------------- \n")
        else:
            not_found_gov_kpi_names.append(kpi_name)
            print(f"🔴Element not found for {kpi_name}🔴\n")

    found_gov_kpi_names.append("Total_NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages")
    found_gov_values.append(Total_NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages)
    found_gov_referance_unit.append("None")
    found_gov_unit_refs.append("None")
    found_gov_periods.append("None")
    found_gov_decimals.append("None")
    not_found_gov_kpi_names.append("None")

    found_gov_kpi_names.append("Total_NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages")
    found_gov_values.append(Total_NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages)
    found_gov_referance_unit.append("None")
    found_gov_unit_refs.append("None")
    found_gov_periods.append("None")
    found_gov_decimals.append("None")
    not_found_gov_kpi_names.append("None")

    found_gov_kpi_names.append("Total_NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages")
    found_gov_values.append(Total_NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages)
    found_gov_referance_unit.append("None")
    found_gov_unit_refs.append("None")
    found_gov_periods.append("None")
    found_gov_decimals.append("None")
    not_found_gov_kpi_names.append("None")

    found_gov_kpi_names.append("Total_NumberOfWorkersForRemunerationOrSalaryOrWages")
    found_gov_values.append(Total_NumberOfWorkersForRemunerationOrSalaryOrWages)
    found_gov_referance_unit.append("None")
    found_gov_unit_refs.append("None")
    found_gov_periods.append("None")
    found_gov_decimals.append("None")
    not_found_gov_kpi_names.append("None")

    print(len(found_gov_kpi_names))
    print(len(found_gov_values))
    print(len(found_gov_referance_unit))
    print(len(found_gov_unit_refs))
    print(len(found_gov_periods))
    print(len(found_gov_decimals))
    print(len(not_found_gov_kpi_names))

    return found_gov_kpi_names, found_gov_values, found_gov_referance_unit, found_gov_unit_refs, found_gov_periods, found_gov_decimals, not_found_gov_kpi_names


