def get_social_data_from_xml(root, namespaces, social_kpi_names):

    # Soical KPIs
    found_env_kpi_names = []
    found_env_referance_unit = []
    found_env_values = []
    found_env_unit_refs = []
    found_env_periods = []
    found_env_decimals = []
    not_found_env_kpi_names = []

    g = 0
    TotalNumberOfTrainingAndAwarenessProgramsHeld_value = 0
    TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value = 0
    TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value = 0

    for kpi_name in social_kpi_names:
        g += 1
        print(f'{g}.')

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

                    if kpi_name == "TotalNumberOfTrainingAndAwarenessProgramsHeld":

                        extended_KPI_Name = f"{kpi_name}_{contextRef}"
                        found_social_kpi_names.append(extended_KPI_Name)
                        found_social_referance_unit.append(contextRef)
                        TotalNumberOfTrainingAndAwarenessProgramsHeld_value += int(value)
                        found_social_values.append(value)
                        found_social_decimals.append(decimal)
                        found_social_unit_refs.append(unit_ref)
                        found_social_periods.append(f"{startPeriod}--{endPeriod}")

                        print("---------------------------- \n")

                    elif kpi_name == "TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues":

                        extended_KPI_Name = f"{kpi_name}_{contextRef}"
                        found_social_kpi_names.append(extended_KPI_Name)
                        found_social_referance_unit.append(contextRef)
                        TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value += int(value)
                        found_social_values.append(value)
                        found_social_decimals.append(decimal)
                        found_social_unit_refs.append(unit_ref)
                        found_social_periods.append(f"{startPeriod}--{endPeriod}")

                        print("---------------------------- \n")

                    elif kpi_name == "PercentageOfPersonsInRespectiveCategoryCoveredByTheAwarenessProgrammes":

                        if contextRef == "D_BoardOfDirectorsSegment":
                            extended_KPI_Name = f"{kpi_name}_{contextRef}"
                            found_social_kpi_names.append(extended_KPI_Name)
                            found_social_referance_unit.append(contextRef)
                            found_social_values.append(f"{float(value)*100}%")
                            found_social_decimals.append(decimal)
                            found_social_unit_refs.append(unit_ref)
                            found_social_periods.append(f"{startPeriod}--{endPeriod}")

                            print("---------------------------- \n")

                        elif contextRef == "D_KeyManagerialPersonnelSegment":
                            extended_KPI_Name = f"{kpi_name}_{contextRef}"
                            found_social_kpi_names.append(extended_KPI_Name)
                            found_social_referance_unit.append(contextRef)
                            found_social_values.append(f"{float(value)*100}%")
                            found_social_decimals.append(decimal)
                            found_social_unit_refs.append(unit_ref)
                            found_social_periods.append(f"{startPeriod}--{endPeriod}")
                            print("---------------------------- \n")

                        elif contextRef == "D_EmployeesOtherThanBoDAndKMPsSegment":
                            extended_KPI_Name = f"{kpi_name}_{contextRef}"
                            found_social_kpi_names.append(extended_KPI_Name)
                            found_social_referance_unit.append(contextRef)
                            found_social_values.append(f"{float(value)*100}%")
                            found_social_decimals.append(decimal)
                            found_social_unit_refs.append(unit_ref)
                            found_social_periods.append(f"{startPeriod}--{endPeriod}")
                            print("---------------------------- \n")

                        elif contextRef == "D_WorkersSegment":
                            extended_KPI_Name = f"{kpi_name}_{contextRef}"
                            found_social_kpi_names.append(extended_KPI_Name)
                            found_social_referance_unit.append(contextRef)
                            found_social_values.append(f"{float(value)*100}%")
                            found_social_decimals.append(decimal)
                            found_social_unit_refs.append(unit_ref)
                            found_social_periods.append(f"{startPeriod}--{endPeriod}")
                            print("---------------------------- \n")

                    elif kpi_name == "ConsumerComplaintsReceivedDuringTheYear":
                        if "2023" in startPeriod.text:                                                         #time perriod check
                            if contextRef == "D_DataPrivacy":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")
                                print("---------------------------- \n")
                            elif contextRef == "D_Other_PY":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")
                                print("---------------------------- \n")
                            elif contextRef == "D_Advertising":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")
                                print("---------------------------- \n")
                            elif contextRef == "D_CyberSecurity":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")
                                print("---------------------------- \n")
                            elif contextRef == "D_DeliveryOfEssentialServices":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")
                                print("---------------------------- \n")
                            elif contextRef == "D_RestrictiveTradePractices":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")
                                print("---------------------------- \n")
                            elif contextRef == "D_UnfairTradePractices":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")
                                print("---------------------------- \n")

                    elif kpi_name == "NumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues":
                        if "2023" in startPeriod.text:                                                         #time perriod check
                            if contextRef == "D_PermanentEmployees_p5":
                                TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value += int(value)
                                print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value}")
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")
                                
                                print("---------------------------- \n")
                            elif contextRef == "D_OtherThanPermanentEmployees_p5":
                                TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value += int(value)
                                print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value}")
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            elif contextRef == "D_Employees_p5":
                                TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value += int(value)
                                print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value}")
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            elif contextRef == "D_PermanentWorkers_p5":
                                TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value += int(value)
                                print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value}")
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            elif contextRef == "D_OtherThanPermanentWorkers_p5":
                                TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value += int(value)
                                print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value}")
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            elif contextRef == "D_Workers_p5":
                                TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value += int(value)
                                print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value}")
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(value)
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            
                    elif kpi_name == "PercentageOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues":
                        if "2023" in startPeriod.text:                                                       #time perriod check
                            if contextRef == "D_PermanentEmployees_p5":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(f"{float(value)*100}%")
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            elif contextRef == "D_OtherThanPermanentEmployees_p5":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(f"{float(value)*100}%")
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            elif contextRef == "D_Employees_p5":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(f"{float(value)*100}%")
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            elif contextRef == "D_PermanentWorkers_p5":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(f"{float(value)*100}%")
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            elif contextRef == "D_OtherThanPermanentWorkers_p5":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(f"{float(value)*100}%")
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")
                            elif contextRef == "D_Workers_p5":
                                extended_KPI_Name = f"{kpi_name}_{contextRef}"
                                found_social_kpi_names.append(extended_KPI_Name)
                                found_social_referance_unit.append(contextRef)
                                found_social_values.append(f"{float(value)*100}%")
                                found_social_decimals.append(decimal)
                                found_social_unit_refs.append(unit_ref)
                                found_social_periods.append(f"{startPeriod}--{endPeriod}")

                                print("---------------------------- \n")

                    elif kpi_name == "NumberOfEmployeesOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment" or kpi_name == "NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment" or kpi_name == "TotalComplaintsReportedUnderSexualHarassmentOfWomenAtWorkplace":
                        if "2023" in startPeriod.text:
                            found_social_kpi_names.append(kpi_name)
                            found_social_referance_unit.append(contextRef)
                            found_social_values.append(value)
                            found_social_decimals.append(decimal)
                            found_social_unit_refs.append(unit_ref)
                            found_social_periods.append(f"{startPeriod}--{endPeriod}")

                            print("---------------------------- \n")
                    
                    elif "Percentage" in kpi_name:
                        found_social_kpi_names.append(kpi_name)
                        found_social_referance_unit.append(contextRef)
                        found_social_values.append(f"{float(value)*100}%")
                        found_social_decimals.append(decimal)
                        found_social_unit_refs.append(unit_ref)
                        found_social_periods.append(f"{startPeriod}--{endPeriod}")
                        
                        print("---------------------------- \n")

                    else:
                        found_social_kpi_names.append(kpi_name)
                        found_social_referance_unit.append(contextRef)
                        found_social_values.append(value)
                        found_social_decimals.append(decimal)
                        found_social_unit_refs.append(unit_ref)
                        found_social_periods.append(f"{startPeriod}--{endPeriod}")
                        
                        print("---------------------------- \n")
        else:
            not_found_social_kpi_names.append(kpi_name)
            print(f"🔴Element not found for {kpi_name}🔴\n")

    found_social_kpi_names.append("Actual_TotalNumberOfTrainingAndAwarenessProgramsHeld_value")
    found_social_values.append(TotalNumberOfTrainingAndAwarenessProgramsHeld_value)
    found_social_referance_unit.append("None")
    found_social_unit_refs.append("None")
    found_social_periods.append("None")
    found_social_decimals.append("None")
    not_found_social_kpi_names.append("None")

    found_social_kpi_names.append("Actual_TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value")
    found_social_values.append(TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value)
    found_social_referance_unit.append("None")
    found_social_unit_refs.append("None")
    found_social_periods.append("None")
    found_social_decimals.append("None")
    not_found_social_kpi_names.append("None")

    found_social_kpi_names.append("Total_NumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value")
    found_social_values.append(TotalNumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value)
    found_social_referance_unit.append("None")
    found_social_unit_refs.append("None")
    found_social_periods.append("None")
    found_social_decimals.append("None")
    not_found_social_kpi_names.append("None")

    print(len(found_social_kpi_names))
    print(len(found_social_values))
    print(len(found_social_referance_unit))
    print(len(found_social_unit_refs))
    print(len(found_social_periods))
    print(len(found_social_decimals))
    print(len(not_found_social_kpi_names))

    return found_social_kpi_names,found_social_kpi_names,found_social_values,found_social_referance_unit,found_social_unit_refs,found_social_periods,found_social_decimals,not_found_social_kpi_names
    