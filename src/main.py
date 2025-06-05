import xml.etree.ElementTree as ET
from KSocial_handeler import get_social_data_from_xml
from KEnvironmental_handeler import get_env_data_from_xml
from KGovernance_handeler import get_gov_data_from_xml
from add_data_to_sheet import adder
from scraper import download_xml_files
from add_data_to_DB import (
    insertion_company,
    insertion_kpi_definition,
    batch_insert_context_references,
    batch_insert_units,
    batch_insert_company_kpi_data,
    insert_aggregated_kpi_data
)

# List of URLs to download

# Original: limit = 20
# User has 6 companies, wants to add 30 more. Total = 36.
# The script will fetch data for 36 companies from the Excel file.
num_already_processed = 5
num_new_to_add = 30
limit_for_download = num_already_processed + num_new_to_add # This is the total number of entries to fetch from Excel

all_company_names, all_file_names, all_urls = download_xml_files('extra_stuff/All_xml_links24_25.xlsx', limit_for_download)

# We only want to process the new companies.
# The first 'num_already_processed' (6) companies will be skipped.
company_names_for_processing = all_company_names[num_already_processed:]
file_names_for_processing = all_file_names[num_already_processed:]
urls_for_processing = all_urls[num_already_processed:]

social_kpi_names = [
    #"TrainingAndAwareness",
    "PercentageOfPersonsInRespectiveCategoryCoveredByTheAwarenessProgrammes",

    #Training and awareness program chart KPIs
    "TotalNumberOfTrainingAndAwarenessProgramsHeld",
    "TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues",
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


inserted_company_ids = []
inserted_kpi_env_definitions_ids = []
inserted_kpi_gov_definitions_ids = []
inserted_kpi_social_definitions_ids = []
total_inserted_company_kpi_data_ids = 0
company_counter = 0
total_social_kpi_names = 0
total_env_kpi_names = 0
total_gov_kpi_names = 0

for company_name, file_name, url in zip(company_names_for_processing, file_names_for_processing, urls_for_processing):
    namespaces = {
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'in-capmkt': 'https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt'
    }

    tree = ET.parse(file_name)
    root = tree.getroot()

    # Get data from handlers
    found_social_kpi_names, found_social_values, found_social_referance_unit, found_social_unit_refs, found_social_periods, found_social_decimals, not_found_social_kpi_names, social_context_refs, found_social_kpi_names_with_contextRef = get_social_data_from_xml(root, namespaces, social_kpi_names)
    found_env_kpi_names, found_env_values, found_env_referance_unit, found_env_unit_refs, found_env_periods, found_env_decimals, not_found_env_kpi_names, env_context_refs, found_env_kpi_names_with_contextRef = get_env_data_from_xml(root, namespaces, env_kpi_names)
    found_gov_kpi_names, found_gov_values, found_gov_referance_unit, found_gov_unit_refs, found_gov_periods, found_gov_decimals, not_found_gov_kpi_names, gov_context_refs, found_gov_kpi_names_with_contextRef = get_gov_data_from_xml(root, namespaces, gov_kpi_names)

    # Insert company
    company_id = insertion_company(company_name, file_name, url)
    inserted_company_ids.append(company_id)

    # Batch insert context references and units
    all_context_refs = env_context_refs + gov_context_refs + social_context_refs
    all_unit_refs = found_env_unit_refs + found_gov_unit_refs + found_social_unit_refs
    context_id_map = batch_insert_context_references(all_context_refs)
    unit_id_map = batch_insert_units(all_unit_refs)

    # Insert KPI definitions
    env_kpi_id_map = insertion_kpi_definition("Environmental", found_env_kpi_names, found_env_unit_refs, found_env_decimals, found_env_referance_unit)
    gov_kpi_id_map = insertion_kpi_definition("Governance", found_gov_kpi_names, found_gov_unit_refs, found_gov_decimals, found_gov_referance_unit)
    social_kpi_id_map = insertion_kpi_definition("Social", found_social_kpi_names, found_social_unit_refs, found_social_decimals, found_social_referance_unit)

    # Batch insert company KPI data
    env_inserted_ids = batch_insert_company_kpi_data(
        company_id, found_env_kpi_names, found_env_values, found_env_periods,
        found_env_referance_unit, found_env_unit_refs, found_env_decimals,
        env_kpi_id_map, context_id_map, unit_id_map
    )
    total_inserted_company_kpi_data_ids += len(env_inserted_ids)

    gov_inserted_ids = batch_insert_company_kpi_data(
        company_id, found_gov_kpi_names, found_gov_values, found_gov_periods,
        found_gov_referance_unit, found_gov_unit_refs, found_gov_decimals,
        gov_kpi_id_map, context_id_map, unit_id_map
    )
    total_inserted_company_kpi_data_ids += len(gov_inserted_ids)

    social_inserted_ids = batch_insert_company_kpi_data(
        company_id, found_social_kpi_names, found_social_values, found_social_periods,
        found_social_referance_unit, found_social_unit_refs, found_social_decimals,
        social_kpi_id_map, context_id_map, unit_id_map
    )
    total_inserted_company_kpi_data_ids += len(social_inserted_ids)

    # Insert aggregated KPIs
    aggregated_kpis = [
        ("Total_NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages", found_gov_values[found_gov_kpi_names.index("Total_NumberOfBoardOfDirectorsForRemunerationOrSalaryOrWages")], gov_kpi_id_map),
        ("Total_NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages", found_gov_values[found_gov_kpi_names.index("Total_NumberOfKeyManagerialPersonnelForRemunerationOrSalaryOrWages")], gov_kpi_id_map),
        ("Total_NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages", found_gov_values[found_gov_kpi_names.index("Total_NumberOfEmployeesOtherThanBodAndKMPForRemunerationOrSalaryOrWages")], gov_kpi_id_map),
        ("Total_NumberOfWorkersForRemunerationOrSalaryOrWages", found_gov_values[found_gov_kpi_names.index("Total_NumberOfWorkersForRemunerationOrSalaryOrWages")], gov_kpi_id_map),
        ("Actual_TotalNumberOfTrainingAndAwarenessProgramsHeld_value", found_social_values[found_social_kpi_names.index("Actual_TotalNumberOfTrainingAndAwarenessProgramsHeld_value")], social_kpi_id_map),
        ("Actual_TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value", found_social_values[found_social_kpi_names.index("Actual_TotalNumberOfEmployeesOrWorkersForTrainingOnHumanRightsIssues_value")], social_kpi_id_map),
        ("Total_NumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value", found_social_values[found_social_kpi_names.index("Total_NumberOfEmployeesOrWorkersCoveredForProvidedTrainingOnHumanRightsIssues_value")], social_kpi_id_map),
        ("Total_NumberOfPersonsBenefittedFromCSRProjects_value", found_social_values[found_social_kpi_names.index("Total_NumberOfPersonsBenefittedFromCSRProjects_value")], social_kpi_id_map),
    ]

    for kpi_name, value, kpi_id_map in aggregated_kpis:
        agg_id = insert_aggregated_kpi_data(company_id, kpi_name, value, kpi_id_map)
        if agg_id:
            total_inserted_company_kpi_data_ids += 1

    # For data visualization in sheets
    adder(found_social_kpi_names, found_social_values, found_social_referance_unit, found_social_unit_refs, found_social_periods, found_social_decimals, not_found_social_kpi_names, company_name, "social info", all_urls)
    adder(found_env_kpi_names, found_env_values, found_env_referance_unit, found_env_unit_refs, found_env_periods, found_env_decimals, not_found_env_kpi_names, company_name, "env_res", all_urls)
    adder(found_gov_kpi_names, found_gov_values, found_gov_referance_unit, found_gov_unit_refs, found_gov_periods, found_gov_decimals, not_found_gov_kpi_names, company_name, "gov info", all_urls)

    company_counter += 1
    total_social_kpi_names += len(found_social_kpi_names)
    total_env_kpi_names += len(found_env_kpi_names)
    total_gov_kpi_names += len(found_gov_kpi_names)

    print(f"total social kpi names = {total_social_kpi_names}")
    print(f"total env kpi names = {total_env_kpi_names}")
    print(f"total gov kpi names = {total_gov_kpi_names}")

print(f"number of companies inserted={len(inserted_company_ids)}")
print(f"number of company kpi data inserted={total_inserted_company_kpi_data_ids}")