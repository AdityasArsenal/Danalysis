import xml.etree.ElementTree as ET
# Step 1: Parse the XML file
tree = ET.parse('nn.xml')
root = tree.getroot()

# Define the namespace map
namespaces = {
    'in-capmkt': 'https://www.sebi.gov.in/xbrl/2024-04-30/in-capmkt'
}

context_ref_value = 'CSRProjectsAxis3'

# Step 2: Use XPath to find the specific tag
element = root.find('.//in-capmkt:TotalScope1Emissions', namespaces=namespaces)
ele1 = root.find('.//in-capmkt:TotalWageCost', namespaces=namespaces)
ele2 = root.find(f'.//in-capmkt:NumberOfPersonsBenefittedFromCSRProjects[@contextRef="{context_ref_value}"]', namespaces=namespaces)

print(ele2.text)
