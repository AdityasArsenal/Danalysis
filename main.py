import xml.etree.ElementTree as ET
from Social_handeler import get_social_data_from_xml
from Environmental_handeler import get_env_data_from_xml
from Governance_handeler import get_gov_data_from_xml
from add_data_to_sheet import adder
from scraper import download_xml_files

# List of URLs to download
company_names,file_names,urls = download_xml_files('All_xml_links24_25.xlsx')

not_found_soc= []
not_found_env= []
not_found_gov= []

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

for company_name,file_name in zip(company_names,file_names):

    namespaces = { 
        'xbrli': 'http://www.xbrl.org/2003/instance',
        'in-capmkt': 'https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt'
    }
    
    tree = ET.parse(file_name)
    root = tree.getroot()

    found_social_kpi_names,found_social_values,found_social_referance_unit,found_social_unit_refs,found_social_periods,found_social_decimals,not_found_social_kpi_names = get_social_data_from_xml(root, namespaces,social_kpi_names)
    
    not_found_soc.extend(not_found_social_kpi_names)
    adder(found_social_kpi_names,found_social_values,found_social_referance_unit,found_social_unit_refs,found_social_periods,found_social_decimals,not_found_social_kpi_names,company_name,"social info",urls)


    found_env_kpi_names,found_env_values,found_env_referance_unit,found_env_unit_refs,found_env_periods,found_env_decimals,not_found_env_kpi_names = get_env_data_from_xml(root, namespaces, env_kpi_names)

    not_found_env.extend(not_found_env_kpi_names)
    adder(found_env_kpi_names,found_env_values,found_env_referance_unit,found_env_unit_refs,found_env_periods,found_env_decimals,not_found_env_kpi_names,company_name,"env_res",urls)


    found_gov_kpi_names, found_gov_values, found_gov_referance_unit, found_gov_unit_refs, found_gov_periods, found_gov_decimals, not_found_gov_kpi_names =  get_gov_data_from_xml(root, namespaces, gov_kpi_names)

    not_found_gov.extend(not_found_gov_kpi_names)
    adder(found_gov_kpi_names, found_gov_values, found_gov_referance_unit, found_gov_unit_refs, found_gov_periods, found_gov_decimals, not_found_gov_kpi_names,company_name,"gov info",urls)

print(len(found_social_kpi_names))
print(len(found_social_unit_refs))
print(len(found_social_decimals))
print(len(found_social_referance_unit))


