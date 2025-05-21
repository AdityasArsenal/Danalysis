import xml.etree.ElementTree as ET
from KSocial_handeler import get_social_data_from_xml
from KEnvironmental_handeler import get_env_data_from_xml
from KGovernance_handeler import get_gov_data_from_xml
from add_data_to_sheet import adder
from scraper import download_xml_files
#from add_data_to_DB import insertion_company,insertion_kpi_definition,insertion_company_kpi_data

# List of URLs to download

limit = 3
company_names,file_names,urls = download_xml_files('extra_stuff/All_xml_links24_25.xlsx',limit)

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
    
    #"EmployeeTurnover",
    "Turnover",
    "TurnoverRate",

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
    
    #"ConsumerProtectionAndGrievances",

    "ConsumerComplaintsReceivedDuringTheYear",
    #"NumberOfConsumerComplaintsInRespectOfTheFollowing", uni ana kpi is ConsumerComplaintsReceivedDuringTheYear
    # "Advertising",
    # "DataPrivacy",
    # "CyberSecurity",
    # "UnfairTradePractices",                               these are the unis
    # "RestrictiveTradePractices",
    # "DeliveryOfEssentialServices",
    
    #"CsrAndSocialResponsibility",
    #"TotalCSRSpend",

    "NumberOfPersonsBenefittedFromCSRProjects",   # need to ask which axis no.
    "jkjk",
    
    #"HumanRightsAndWorkplaceEthics",

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
    
    #"OtherHumanRightsRelatedIssues"
]
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
    'WasteDisposedByOtherDisposalOperations',
    'TotalFuelConsumptionFromNonRenewableSources',
    'TotalFuelConsumptionFromRenewableSources',
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
    'asefasd',
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
    'TotalVolumeOfWaterConsumption'
    'WasteRecoveredThroughRecycled'
    
]
gov_kpi_names = [
    "EthicalSourcingAndSupplyChain",
    "PercentageOfInputsWereSourcedSustainably",
    #"BoardAndLeadershipDiversity", calculating on the last data
    "TotalNumberOfBoardOfDirectors",
    "NumberOfFemaleBoardOfDirectors",
    "TotalNumberOfKeyManagementPersonnel",
    "NumberOfFemaleKeyManagementPersonnel",
    "DoesTheEntityHaveAFrameworkOrPolicyOnCyberSecurityAndRisksRelatedToDataPrivacy",
    "WebLinkOfThePolicyOnCyberSecurityAndRisksRelatedToDataPrivacy",
    "NumberOfInstancesOfDataBreachesAlongWithImpact",
    "TotalNumberOfInstancesOfDataBreaches", #Not found anyware

    "TotalWagesPaid",

    "RemunerationAndPayEquity", # decide on the following data
    # "MedianRemunerationSalaryWagesOfBoardOfDirectorsFemale",
    # "MedianRemunerationSalaryWagesOfBoardOfDirectorsMale",
    # "MedianRemunerationSalaryWagesOfKeyManagerialPersonnelFemale",
    # "MedianRemunerationSalaryWagesOfKeyManagerialPersonnelMale",
    # "MedianRemunerationSalaryWagesOfEmployeesOtherThanBODAndKMPFemale",
    "MedianRemunerationSalaryWagesOfEmployeesOtherThanBODAndKMPMale"
        
    "NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfBoardOfDirectors",

    "NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfKeyManagerialPersonnel",

    "NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfEmployeesOtherThanBodAndKMP",

    "NumberOfWorkersForRemunerationOrSalaryOrWages",
    "MedianOfRemunerationOrSalaryOrWagesOfWorkers",
]

inserted_company_names = []
inserted_company_ids = []

inserted_kpi_env_names = []
inserted_kpi_env_definitions_ids = []

inserted_kpi_gov_names = []
inserted_kpi_gov_definitions_ids = []

inserted_kpi_social_names = []
inserted_kpi_social_definitions_ids = []

total_inserted_company_kpi_data_ids = 0

company_counter = 0
total_social_kpi_names = 0
total_env_kpi_names = 0               #to check how many kpi are found IN TOTAL
total_gov_kpi_names = 0

for company_name,file_name in zip(company_names,file_names):
    namespaces = { 
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'in-capmkt': 'https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt'
    }
    

    tree = ET.parse(file_name)
    root = tree.getroot()
    
    found_social_kpi_names,found_social_values,found_social_referance_unit,found_social_unit_refs,found_social_periods,found_social_decimals,not_found_social_kpi_names = get_social_data_from_xml(root, namespaces,social_kpi_names)
    found_env_kpi_names,found_env_values,found_env_referance_unit,found_env_unit_refs,found_env_periods,found_env_decimals,not_found_env_kpi_names = get_env_data_from_xml(root, namespaces, env_kpi_names)
    found_gov_kpi_names, found_gov_values, found_gov_referance_unit, found_gov_unit_refs, found_gov_periods, found_gov_decimals, not_found_gov_kpi_names =  get_gov_data_from_xml(root, namespaces, gov_kpi_names)

    for found_social_kpi_name,found_social_value in zip(found_social_kpi_names,found_social_values):
        print(f"{found_social_kpi_name}----=----{found_social_value}")
        print(f"{company_name}")
    print("--------------------------------")

    for found_env_kpi_name,found_env_value in zip(found_env_kpi_names,found_env_values):              #TO MAKE SURE THE DATA IS CORRECT
        print(f"{found_env_kpi_name}----=----{found_env_value}")

    print("--------------------------------")

    for found_gov_kpi_name,found_gov_value in zip(found_gov_kpi_names,found_gov_values):
        print(f"{found_gov_kpi_name}----=----{found_gov_value}")



    company_counter += 1

    total_social_kpi_names += len(found_social_kpi_names)
    total_env_kpi_names += len(found_env_kpi_names)                 #to check how many kpi are found IN TOTAL
    total_gov_kpi_names += len(found_gov_kpi_names)

    print(f"total social kpi names = {total_social_kpi_names}")
    print(f"total env kpi names = {total_env_kpi_names}")           #to check how many kpi are found IN TOTAL
    print(f"total gov kpi names = {total_gov_kpi_names}")


    # inserted_company_id = insertion_company(company_name)
    # inserted_company_ids.append(inserted_company_id)
    # inserted_company_names.append(company_name)


    # insertion_kpi_definition("79aa665d-fdf5-4ad4-8550-727590914348", found_env_kpi_names, found_env_unit_refs, found_env_decimals,found_env_referance_unit,inserted_kpi_env_names,inserted_kpi_env_definitions_ids)
    # insertion_kpi_definition("8f7b1de0-ff85-4d90-84af-61119dc77b39", found_gov_kpi_names, found_gov_unit_refs, found_gov_decimals,found_gov_referance_unit,inserted_kpi_gov_names,inserted_kpi_gov_definitions_ids) 
    # insertion_kpi_definition("f4f14038-ce0e-46ca-b453-d421a90e191b", found_social_kpi_names, found_social_unit_refs, found_social_decimals, found_social_referance_unit,inserted_kpi_social_names,inserted_kpi_social_definitions_ids)


    # inserted_company_kpi_data_idss = insertion_company_kpi_data(inserted_company_id, found_env_kpi_names, inserted_kpi_env_names, inserted_kpi_env_definitions_ids, found_env_values, found_env_periods)
    # total_inserted_company_kpi_data_ids += len(inserted_company_kpi_data_idss)

    # inserted_company_kpi_data_idss = insertion_company_kpi_data(inserted_company_id, found_gov_kpi_names, inserted_kpi_gov_names, inserted_kpi_gov_definitions_ids, found_gov_values, found_gov_periods)
    # total_inserted_company_kpi_data_ids += len(inserted_company_kpi_data_idss)

    # inserted_company_kpi_data_idss = insertion_company_kpi_data(inserted_company_id, found_social_kpi_names, inserted_kpi_social_names, inserted_kpi_social_definitions_ids, found_social_values, found_social_periods)
    # total_inserted_company_kpi_data_ids += len(inserted_company_kpi_data_idss)


    # FOR DATA VISULIZATION ADDED INTO SHEETS 
    adder(found_social_kpi_names,found_social_values,found_social_referance_unit,found_social_unit_refs,found_social_periods,found_social_decimals,not_found_social_kpi_names,company_name,"social info",urls)
    adder(found_env_kpi_names,found_env_values,found_env_referance_unit,found_env_unit_refs,found_env_periods,found_env_decimals,not_found_env_kpi_names,company_name,"env_res",urls)
    adder(found_gov_kpi_names, found_gov_values, found_gov_referance_unit, found_gov_unit_refs, found_gov_periods, found_gov_decimals, not_found_gov_kpi_names,company_name,"gov info",urls)

print("+++++++++++++++++++++++++++")
print(f"number of companies inserted={len(inserted_company_names)}")
print(f"number of env kpi inserted={len(inserted_kpi_env_definitions_ids)}")
print(f"number of gov kpi inserted={len(inserted_kpi_gov_definitions_ids)}")
print(f"number of social kpi inserted={len(inserted_kpi_social_definitions_ids)}")
print(f"number of company kpi data inserted={total_inserted_company_kpi_data_ids}")



#to check the data inserted in the database
# for inserted_company_name,inserted_company_id, inserted_kpi_env_name, inserted_kpi_env_definitions_id, inserted_kpi_gov_name, inserted_kpi_gov_definitions_id, inserted_kpi_social_name, inserted_kpi_social_definitions_id in zip(inserted_company_names,inserted_company_ids,inserted_kpi_env_names[0:5],inserted_kpi_env_definitions_ids[0:5],inserted_kpi_gov_names[0:5],inserted_kpi_gov_definitions_ids[0:5],inserted_kpi_social_names[0:5],inserted_kpi_social_definitions_ids[0:5]):

#     print(f"{inserted_company_name}-{inserted_company_id}")
#     print("================================")
#     print(f"{inserted_kpi_env_name}-{inserted_kpi_env_definitions_id}")
#     print("--------------------------------")
#     print(f"{inserted_kpi_gov_name}-{inserted_kpi_gov_definitions_id}")
#     print("--------------------------------")
#     print(f"{inserted_kpi_social_name}-{inserted_kpi_social_definitions_id}")
#     print("--------------------------------")




