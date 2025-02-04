import xml.etree.ElementTree as ET

tree = ET.parse('xml_files/nn.xml')
root = tree.getroot()

namespaces = {
    'xbrli': 'http://www.xbrl.org/2003/instance',
    'in-capmkt': 'https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt'
}

social_kpi_names = [
    #"TrainingAndAwareness",
    "TotalNumberOfTrainingAndAwarenessProgramsHeld",
    "TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues",

    "PercentageOfPersonsInRespectiveCategoryCoveredByTheAwarenessProgrammes",
    # "PercentOfPersonsCoveredByTrainingAndAwarenessProgrammesWorkers",
    # "PercentOfPersonsCoveredByTrainingAndAwarenessProgrammesBoardOfDirectors",                #neeeds unit check
    # "PercentOfPersonsCoveredByTrainingAndAwarenessProgrammesKeyManagerialPersonnelKMPs",
    # "PercentOfPersonsCoveredByTrainingAndAwarenessProgrammesEmployeesOtherThanKMPsAndBODs",
    
    "PercentageOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues", #uni anna 
    #"PercentOfPermanentEmployeesProvidedTrainingOnHumanRightsIssuesAndPolicies",

    
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

def get_social_data_from_xml(root, namespaces, social_kpi_names):
    g = 0
    TotalNumberOfTrainingAndAwarenessProgramsHeld_value = 0
    TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value = 0

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

                        print(f"KPI Name: {kpi_name}_{contextRef}")
                        print(f"referance_unit : {contextRef}")
                        TotalNumberOfTrainingAndAwarenessProgramsHeld_value += int(value)
                        print(f"Value: {value}")
                        print(f"Decimals: {decimal}")
                        print(f"unit : {unit_ref}")
                        print("---------------------------- \n")

                    elif kpi_name == "TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues":

                        print(f"KPI Name: {kpi_name}_{contextRef}")
                        print(f"referance_unit : {contextRef}")
                        TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value += int(value)
                        print(f"Value: {value}")
                        print(f"Decimals: {decimal}")
                        print(f"unit : {unit_ref}")
                        print("---------------------------- \n")

                    elif kpi_name == "PercentageOfPersonsInRespectiveCategoryCoveredByTheAwarenessProgrammes":

                        if contextRef == "D_BoardOfDirectorsSegment":
                            print(f"KPI Name: {kpi_name}_{contextRef}")
                            print(f"referance_unit : {contextRef}")
                            TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value += int(value)
                            print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value}")
                            print(f"Value: {value}")
                            print(f"Decimals: {decimal}")
                            print(f"unit : {unit_ref}")
                            print("---------------------------- \n")

                        elif contextRef == "D_KeyManagerialPersonnelSegment":
                            print(f"KPI Name: {kpi_name}_{contextRef}")
                            print(f"referance_unit : {contextRef}")
                            TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value += int(value)
                            print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value}")
                            print(f"Value: {value}")
                            print(f"Decimals: {decimal}")
                            print(f"unit : {unit_ref}")
                            print("---------------------------- \n")

                        elif contextRef == "D_EmployeesOtherThanBoDAndKMPsSegment":
                            print(f"KPI Name: {kpi_name}_{contextRef}")
                            print(f"referance_unit : {contextRef}")
                            TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value += int(value)
                            print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value}")
                            print(f"Value: {value}")
                            print(f"Decimals: {decimal}")
                            print(f"unit : {unit_ref}")
                            print("---------------------------- \n")

                        elif contextRef == "D_WorkersSegment":
                            print(f"KPI Name: {kpi_name}_{contextRef}")
                            print(f"referance_unit : {contextRef}")
                            TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value +=  int(float(value))
                            print(f"Total_Value: {TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value}")
                            print(f"Value: {value}")
                            print(f"Decimals: {decimal}")
                            print(f"unit : {unit_ref}")
                            print("---------------------------- \n")

                    else:
                        # print(f"KPI Name: {kpi_name}")
                        # print(f"Value: {value}")
                        # print(f"unit : {unit_ref})
                        # print(f"Decimals: {decimal}")
                         print("---------------------------- \n")
                else:
                    print(f"🔴Element not found for {kpi_name}🔴\n")

    print(f"Actual_TotalNumberOfTrainingAndAwarenessProgramsHeld_value : {TotalNumberOfTrainingAndAwarenessProgramsHeld_value}")
    print(f"Actual_TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value : { TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value}")

get_social_data_from_xml(root, namespaces, social_kpi_names)