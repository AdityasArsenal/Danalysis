import xml.etree.ElementTree as ET
# Step 1: Parse the XML file
tree = ET.parse('nn.xml')
root = tree.getroot()

# Define the namespace map
namespaces = {
    'in-capmkt': 'https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt'
}

# Step 2: Use XPath to find the specific tag
ele0 = root.find('.//in-capmkt:TotalScope1Emissions', namespaces=namespaces)
ele1 = root.find('.//in-capmkt:TotalWageCost', namespaces=namespaces)
ele2 = root.find('.//in-capmkt:NumberOfPersonsBenefittedFromCSRProjects', namespaces=namespaces)

# Step 3: Check if the tag is found and extract information
if ele0 is not None:

    print("Attributes:")
    for attr, value in ele0.attrib.items():
        print(f"{attr}: {value}")
        
    print("-----------")

    context_ref = ele0.get('contextRef')
    cn = ele1.get('contextRef')

    decimals = ele0.get('decimals')
    decimals1 = ele1.get('decimals')

    period = ele0.get('endDate')
    period1 = ele1.get('endDate')

    unit_ref = ele0.get('unitRef')
    unit_ref1 = ele1.get('unitRef')

    amount = ele0.text
    amount1 = ele1.text

    print(f"Unit: {context_ref}")
    print(f"Decimals: {decimals}")
    print(f"Priod: {period}")
    print(f"UnitRef: {unit_ref}")
    print(f"Amount: {amount}")

    print("the second kip")

    print(f"Unit: {cn}")
    print(f"Decimals: {decimals1}")
    print(f"Priod: {period1}")
    print(f"UnitRef: {unit_ref1}")
    print(f"Amount: {amount1}")


    print("*********************")
    print(ele2.text)
else:
    print("Element 'TotalScope1Emissions' not found")