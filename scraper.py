import requests

url = "https://nsearchives.nseindia.com/corporate/xbrl/BRSR_1345203_14012025053859_WEB.xml"

response = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})
response.raise_for_status()

with open("BRSR.xml", "wb") as f:
    f.write(response.content)
print("File saved as BRSR.xml")