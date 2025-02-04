import xml.etree.ElementTree as ET

tree = ET.parse('xml_files/nn.xml')
root = tree.getroot()

namespaces = {
    'xbrli': 'http://www.xbrl.org/2003/instance',
    'in-capmkt': 'https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt'
}

env_kpi_names = [
    'GreenhouseGasGHGEmissions',#####
    'WhetherDetailsOfGreenHouseGasEmissionsAndItsIntensityIsApplicableToTheCompany',
    'TotalScope1Emissions',
    'TotalScope2Emissions',
    'TotalScope3Emissions',
    'TotalScope3EmissionsPerRupeeOfTurnover',#####
    'TotalScope1EndScope2EmissionsPerRupeeOfTurnover',
    'WasteManagement',#####
    'TotalWasteGenerated',
    'TotalWasteDisposed',
    'Landfilling',
    'WasteDisposedByLandfilling',
    'WasteDisposedByIncineration',
    'EWaste',
    'BatteryWaste',
    'PlasticWaste',
    'BioMedicalWaste',
    'RadioactiveWaste',
    'OtherHazardousWaste',
    'ConstructionAndDemolitionWaste',
    'OtherNonHazardousWasteGenerated',
    'WasteIntensityPerRupeeOfTurnover',
    'TotalWasteRecovered',
    'WasteRecoveredThroughReUsed',
    'AmountOfReUsed',
    'AmountOfRecycled',
    'WasteRecoveredThroughRecycled',
    'WaterManagement',#####
    'TotalWaterDischargedInKilolitres',
    'TotalWaterWithdrawal',#####
    'WaterWithdrawalBySurfaceWater',
    'WaterWithdrawalByGroundwater',
    'WaterWithdrawalByThirdPartyWater',
    'WaterWithdrawalBySeawaterDesalinatedWater',#####
    'WaterWithdrawalByOther',#####
    'TotalWaterConsumption',#####
    'TotalWaterDischargedInKilolitres',
    'TotalWaterDischargedToGroundwaterWithTreatment',#####removable
    'WaterDischargeToGroundwaterWithOutTreatment',
    'WaterDischargeToSurfaceWaterWithTreatment',
    'WaterDischargeToSurfaceWaterWithOutTreatment',
    'WaterDischargeToSeawaterWithTreatment',
    'WaterDischargeToSeawaterWithOutTreatment',
    'WaterDischargeToThirdPartiesWithTreatment',##
    'WaterDischargeToThirdPartiesWithoutTreatment',##
    'WaterDischargeToOthersWithTreatment',
    'WaterDischargeToOthersWithoutTreatment',
    'WaterRecovered',#####
    'WaterIntensityPerRupeeOfTurnover',
    'EnergyManagement',#####
    'TotalEnergyConsumedFromRenewableSources',
    'TotalEnergyConsumedFromRenewableAndNonRenewableSources',
    'TotalEnergyConsumedFromNonRenewableSources',
    'EnergyIntensityPerRupeeOfTurnover'
]
social_kpi_names =[
    #"TrainingAndAwareness",
    "TotalNumberOfTrainingAndAwarenessProgramsHeld",
    "TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues",

    "PercentageOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues", #uni anna 
    #"PercentOfPermanentEmployeesProvidedTrainingOnHumanRightsIssuesAndPolicies",

    "TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues",
    "PercentageOfPersonsInRespectiveCategoryCoveredByTheAwarenessProgrammes",
    # "PercentOfPersonsCoveredByTrainingAndAwarenessProgrammesWorkers",
    # "PercentOfPersonsCoveredByTrainingAndAwarenessProgrammesBoardOfDirectors",                #neeeds unit check
    # "PercentOfPersonsCoveredByTrainingAndAwarenessProgrammesKeyManagerialPersonnelKMPs",
    # "PercentOfPersonsCoveredByTrainingAndAwarenessProgrammesEmployeesOtherThanKMPsAndBODs",
    
    #"TotalNumberOfTrainingsGivenToEmployeesMale",
    #"TotalNumberOfTrainingsGivenToEmployeesFemale",                        #no mention of training in any sheet
    
    #"WorkforceAndEmployment",
    "NumberOfEmployeesOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment",
    "NumberOfWorkersOrWhoseFamilyMembersRehabilitatedAndPlacedInSuitableEmployment",

    # "TotalNumberOfPermanentWorkersMaleAtTheEndOfTheFY",
    # "TotalNumberOfPermanentEmployeesMaleAtTheEndOfTheFY",
    # "TotalNumberOfPermanentWorkersFemaleAtTheEndOfTheFY",           #UNIT ANALYSIS   add all the values where unit has PermanentWorkers
    # "TotalNumberOfPermanentEmployeesFemaleAtTheEndOfTheFY",
    # "TotalNumberOfWorkersIncludingDifferentlyAbledAtTheEndOfTheFY",
    # "TotalNumberOfEmployeesIncludingDifferentlyAbledAtTheEndOfTheFY",
    
    "EmployeeTurnover",


    # "TotalTurnoverRateForMalePermanentEmployees",
    # "TotalTurnoverRateForFemalePermanentEmployees",                       unit ann but kpi is "TurnoverRate"

    #"Health & Safety",
    "WhetherAnOccupationalHealthAndSafetyManagementSystemHasBeenImplementedByTheEntity",
    "DetailsOfOccupationalHealthAndSafetyManagementSystemExplanatoryTextBlock",
    "PercentageOfHealthAndSafetyPracticesOfYourPlantsAndOfficesThatWereAssessedP3",

    # "NumberOfFatalitiesWorkers",                          uni ana kpi is NumberOfFatalities
    # "NumberOfFatalitiesEmployees",
    
    #"TotalRecordableWorkRelatedInjuriesWorkers",           #unit ana kpi is "TotalRecordableWorkRelatedInjuries"
    #"TotalRecordableWorkRelatedInjuriesEmployees",
    
    #"LostTimeInjuryFrequencyRateLTIFRWorkers",             uni ana kpi is "LostTimeInjuryFrequencyRatePerOneMillionPersonHoursWorked" 
    #"LostTimeInjuryFrequencyRateLTIFREmployees",
    
    # "HighConsequenceWorkRelatedInjuryOrIllHealthExcludingFatalitiesWorkers",
    # "HighConsequenceWorkRelatedInjuryOrIllHealthExcludingFatalitiesEmployees",        # kpi is HighConsequenceWorkRelatedInjuryOrIllHealthExcludingFatalities
   
    # "NumberOfComplaintsAboutHealthAndSafetyPendingResolutionAtYearEnd",
    # "NumberOfComplaintsAboutWorkingConditionsPendingResolutionAtYearEnd",
    # "NumberOfComplaintsAboutHealthAndSafetyFiledByEmployeesAndWorkersDuringTheYear",
    # "NumberOfComplaintsAboutWorkingConditionsFiledByEmployeesAndWorkersDuringTheYear",
    
    "ConsumerProtectionAndGrievances",
    #"NumberOfConsumerComplaintsInRespectOfTheFollowing", uni ana kpi is ConsumerComplaintsReceivedDuringTheYear
    # "Advertising",
    # "DataPrivacy",
    # "CyberSecurity",
    # "UnfairTradePractices",                               these are the unis
    # "RestrictiveTradePractices",
    # "DeliveryOfEssentialServices",
    
    #"CsrAndSocialResponsibility",
    #"TotalCSRSpend",

    "NumberOfPersonsBenefittedFromCSRProjects",
    
    "HumanRightsAndWorkplaceEthics",

    "NumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues", #UNI as it has prymary and others

    #"NumberOfComplaintsOnTheFollowingFiledByEmployeesAndWorkers",

    #"NumberOfComplaintsFiledDuringTheYear",


    #"Wages",                   unit ana kpi is TotalWageCost

    #"ChildLabour",
    "PercentageOfChildLabourOfYourPlantsAndOfficesThatWereAssessedP5",
    "PercentageOfChildLabourOfValueChainPartnersP5",

    "TotalComplaintsReportedUnderSexualHarassmentOfWomenAtWorkplace",

    #"DiscriminationAtWorkplace",
    "PercentageOfDiscriminationAtWorkPlaceOfYourPlantsAndOfficesThatWereAssessedP5",
    "PercentageOfDiscriminationAtWorkPlaceOfValueChainPartnersP5",

    #"ForcedLabourInvoluntaryLabour",
    "PercentageOfForcedLabourOrInvoluntaryLabourOfValueChainPartnersP5",
    "PercentageOfForcedLabourOrInvoluntaryLabourOfYourPlantsAndOfficesThatWereAssessedP5",
    
    "OtherHumanRightsRelatedIssues"
]
governance_kpi_names = [
    "EthicalSourcingAndSupplyChain",
    "PercentageOfInputsWereSourcedSustainably",
    "BoardAndLeadershipDiversity",
    "TotalNumberOfBoardOfDirectors",
    "NumberOfFemaleBoardOfDirectors",
    "TotalNumberOfKeyManagementPersonnel",
    "NumberOfFemaleKeyManagementPersonnel",
    "DoesTheEntityHaveAFrameworkOrPolicyOnCyberSecurityAndRisksRelatedToDataPrivacy",
    "WebLinkOfThePolicyOnCyberSecurityAndRisksRelatedToDataPrivacy",
    "NumberOfInstancesOfDataBreachesAlongWithImpact",
    "TotalNumberOfInstancesOfDataBreaches",

    "RemunerationAndPayEquity",
    "MedianRemunerationSalaryWagesOfBoardOfDirectorsFemale",
    "MedianRemunerationSalaryWagesOfBoardOfDirectorsMale",
    "MedianRemunerationSalaryWagesOfKeyManagerialPersonnelFemale",
    "MedianRemunerationSalaryWagesOfKeyManagerialPersonnelMale",
    "MedianRemunerationSalaryWagesOfEmployeesOtherThanBODAndKMPFemale",
    "MedianRemunerationSalaryWagesOfEmployeesOtherThanBODAndKMPMale"
        
    "NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfBoardOfDirectors",
    "NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfBoardOfDirectors",
    "NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfBoardOfDirectors",
    "NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfKeyManagerialPersonnel",
    "NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfKeyManagerialPersonnel",
    "NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfKeyManagerialPersonnel",
    "NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfEmployeesOtherThanBodAndKMP",
    "NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfEmployeesOtherThanBodAndKMP",
    "NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfEmployeesOtherThanBodAndKMP",
    "NumberOfWorkersForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfWorkers",
    "NumberOfWorkersForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfWorkers",
    "NumberOfWorkersForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfWorkers",
]



def get_data_from_xml(root, namespaces, env_kpi_names, social_kpi_names, governance_kpi_names):

    # Environmental KPIs
    found_env_kpi_names = []
    found_env_values = []
    found_env_unit_refs = []
    found_env_periods = []
    found_env_decimals = []
    not_found_env_kpi_names = []

    # Soical KPIs
    found_social_kpi_names = []
    found_social_values = []
    found_social_unit_refs = []
    found_social_periods = []
    found_social_decimals = []
    not_found_social_kpi_names = []

    # Governance KPIs
    found_governance_kpi_names = []
    found_governance_values = []
    found_governance_unit_refs = []
    found_governance_periods = []
    found_governance_decimals = []
    not_found_governance_kpi_names = []
    
    def get_env_data_from_xml(root, namespaces, env_kpi_names):
        e = 0
        for kpi_name in env_kpi_names:
            e += 1
            print(f'{e}.')

            element = root.find(f'.//in-capmkt:{kpi_name}', namespaces=namespaces)

            if element is not None:

                contextRef = element.get('contextRef')                                                                      # Get contextRef from element to get the period
                period_element = root.find(f'.//xbrli:context[@id="{contextRef}"]/xbrli:period', namespaces=namespaces)    # Get period element using contextRef

                decimal = element.get('decimals')
                unit_ref = element.get('unitRef')
                if period_element is not None:
                    startPeriod = period_element.find('xbrli:startDate', namespaces=namespaces)
                    endPeriod = period_element.find('xbrli:endDate', namespaces=namespaces)
                else:
                    period = 'NA'

                if unit_ref == 'MtCO2e':                                                             # unit handling  (Convert MtCO2e to tCO2e)
                    value = float(element.text) * 1000000
                    unit_ref = 'tCO2e'                                                              
                elif unit_ref == 'MtCO2ePerINR':
                    value = float(element.text) * 1000000
                    unit_ref = 'tCO2e/INR crore'
                elif unit_ref == 'Kilojoule':
                    value = float(element.text) /1000
                    unit_ref = 'gigajoules'
                elif unit_ref == 'KilojoulePerINR':
                    value = float(element.text) /1000
                    unit_ref = 'gigajoules/INR crore'
                else:
                    value = element.text

                found_env_kpi_names.append(kpi_name)
                found_env_values.append(value)
                found_env_unit_refs.append(unit_ref)
                found_env_periods.append(f"{startPeriod.text}-{endPeriod.text}")
                found_env_decimals.append(decimal)
            
            else:
                not_found_env_kpi_names.append(kpi_name)
                print(f"🔴Element not found for {kpi_name}🔴\n")

    def get_social_data_from_xml(root, namespaces, social_kpi_names):
        
        g = 0
        for kpi_name in social_kpi_names:
            g += 1
            print(f'{g}.')

            element = root.find(f'.//in-capmkt:{kpi_name}', namespaces=namespaces)

            if element is not None:

                contextRef = element.get('contextRef')                                                                      # Get contextRef from element to get the period
                period_element = root.find(f'.//xbrli:context[@id="{contextRef}"]/xbrli:period', namespaces=namespaces)    # Get period element using contextRef

                decimal = element.get('decimals')
                unit_ref = element.get('unitRef')
                value = element.text

                if period_element is not None:
                    startPeriod = period_element.find('xbrli:startDate', namespaces=namespaces)
                    endPeriod = period_element.find('xbrli:endDate', namespaces=namespaces)
                else:
                    period = 'NA'

                found_social_kpi_names.append(kpi_name)
                found_social_values.append(value)
                found_social_unit_refs.append(unit_ref)
                found_social_periods.append(f"{startPeriod.text}-{endPeriod.text}")
                found_social_decimals.append(decimal)
            
            else:
                not_found_social_kpi_names.append(kpi_name)
                print(f"🔴Element not found for {kpi_name}🔴\n")

    def get_governance_data_from_xml(root, namespaces, governance_kpi_names):
        g = 0
        for kpi_name in governance_kpi_names:
            g += 1
            print(f'{g}.')

            element = root.find(f'.//in-capmkt:{kpi_name}', namespaces=namespaces)

            if element is not None:
                contextRef = element.get('contextRef')
                period_element = root.find(f'.//xbrli:context[@id="{contextRef}"]/xbrli:period', namespaces=namespaces)

                decimal = element.get('decimals')
                unit_ref = element.get('unitRef')
                value = element.text

                if period_element is not None:
                    startPeriod = period_element.find('xbrli:startDate', namespaces=namespaces)
                    endPeriod = period_element.find('xbrli:endDate', namespaces=namespaces)
                else:
                    period = 'NA'

                found_governance_kpi_names.append(kpi_name)
                found_governance_values.append(value)
                found_governance_unit_refs.append(unit_ref)
                found_governance_periods.append(f"{startPeriod.text}-{endPeriod.text}")
                found_governance_decimals.append(decimal)
            
            else:
                not_found_governance_kpi_names.append(kpi_name)
                print(f"🔴Element not found for {kpi_name}🔴\n")

    get_env_data_from_xml(root, namespaces, env_kpi_names)
    print(len(found_env_kpi_names), len(found_env_values), len(found_env_unit_refs), len(found_env_periods), len(found_env_decimals))
    print(f"🟢🟢🟢🟢🟢🟢🟢🟢env info🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢")

    get_social_data_from_xml(root, namespaces, social_kpi_names)
    print(len(found_social_kpi_names), len(found_social_values), len(found_social_unit_refs), len(found_social_periods), len(found_social_decimals))
    print(f"🟢🟢🟢🟢🟢🟢🟢🟢🟢social info🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢")

    get_governance_data_from_xml(root, namespaces, governance_kpi_names)
    print(len(found_governance_kpi_names), len(found_governance_values), len(found_governance_unit_refs), len(found_governance_periods), len(found_governance_decimals))
    print(f"🟢🟢🟢🟢🟢🟢🟢🟢🟢governance info🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢")


get_data_from_xml(root, namespaces, env_kpi_names, social_kpi_names, governance_kpi_names)
