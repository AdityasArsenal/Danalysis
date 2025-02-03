import xml.etree.ElementTree as ET

tree = ET.parse('gg.xml')
root = tree.getroot()

namespaces = {
    'xbrli': 'http://www.xbrl.org/2003/instance',
    'in-capmkt': 'https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt'
}

kpi_names = [
    'GreenhouseGas_GHG_Emissions',
    'TotalScope1Emissions',
    'TotalScope2Emissions',
    'TotalScope3Emissions',
    'TotalScope3EmissionsPerRupeeOfTurnover',
    'TotalScope1EndScope2EmissionsPerRupeeOfTurnover',
    'WasteManagement',
    'TotalWasteGenerated',
    'TotalWasteDisposed',
    'Landfilling',
]

units = [
    '',
    'tCO2e',
    'tCO2e',
    'tCO2e',
    'tCO2e/INR crore',
    'tCO2e/INR crore',
    '',
    'tonne',
    'tonne',
    'tonne',
]


def get_data_from_xml(root, units, namespaces, kpi_names):

    c = 0
    for kpi_name,unit in zip(kpi_names,units):
        c += 1
        print(f'{c}.')

        element = root.find(f'.//in-capmkt:{kpi_name}', namespaces=namespaces)

        if element is not None:

            contextRef = element.get('contextRef')                                                                      # Get contextRef from element to get the period
            period_element = root.find(f'.//xbrli:context[@id="{contextRef}"]/xbrli:period', namespaces=namespaces)    # Get period element using contextRef

            decimals = element.get('decimals')
            unit_ref = element.get('unitRef')
            if period_element is not None:
                startPeriod = period_element.find('xbrli:startDate', namespaces=namespaces)
                endPeriod = period_element.find('xbrli:endDate', namespaces=namespaces)
            else:
                period = None

            if unit_ref == 'MtCO2e':                                                            # Convert MtCO2e to tCO2e
                value = float(element.text) * 1000000
                unit_ref = 'tCO2e'                                                              # unit handling
            else:
                value = element.text

            #print(f"Unit: {unit}")
            print(f"KPI Name: {kpi_name}")
            print(f"Decimals: {decimals}")
            print(f"Priod: {startPeriod.text}-{endPeriod.text}")
            print(f"UnitRef: {unit_ref}")

            print(f"\nText content: {value}")
            print(f"-----------------------------------\n")
        
        else:
            print(f"🔴Element not found for {kpi_name}🔴\n")

get_data_from_xml(root, units, namespaces, kpi_names)
