import xml.etree.ElementTree as ET

# Step 1: Parse the XML file
tree = ET.parse('nn.xml')
root = tree.getroot()

# Define the namespace map
namespaces = {
    'xbrli': 'http://www.xbrl.org/2003/instance',
    'in-capmkt': 'https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt'
}

# Define the contextRef value you are looking for
context_ref_value = 'CSRProjectsAxis3'  # Replace with the actual contextRef value

# Step 2: Use XPath to find the specific tag by tag name and attribute
element = root.find(f'.//in-capmkt:NumberOfPersonsBenefittedFromCSRProjects[@contextRef="{context_ref_value}"]', namespaces=namespaces)

# Step 3: Check if the tag is found and extract information
if element is not None:
    # Print attributes
    print("Attributes:")
    for attr, value in element.attrib.items():
        print(f"{attr}: {value}")

    # Print text content
    print(f"\nText content: {element.text}")

    # Find and print the Period element
    period_element = root.find(f'.//xbrli:context[@id="{context_ref_value}"]/xbrli:period', namespaces=namespaces)
    if period_element is not None:
        start_date = period_element.find('xbrli:startDate', namespaces=namespaces)
        end_date = period_element.find('xbrli:endDate', namespaces=namespaces)
        instant = period_element.find('xbrli:instant', namespaces=namespaces)
        
        if start_date is not None:
            print(f"Start Date: {start_date.text}")
        if end_date is not None:
            print(f"End Date: {end_date.text}")
        if instant is not None:
            print(f"Instant: {instant.text}")
    else:
        print("Period element not found")
else:
    print("Element 'NumberOfPersonsBenefittedFromCSRProjects' not found")