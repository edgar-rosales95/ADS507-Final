import requests
import pandas as pd

API_KEY = '****'

url = 'https://api.census.gov/data/2019/pep/housing'

params = {
    'get': 'DATE_CODE,NAME,HUEST,DATE_DESC',
    'for': 'county:195',
    'in': 'state:02',
    "key": API_KEY
}

response = requests.get(url, params=params)

data = response.json()
df = pd.DataFrame(data[1:], columns=data[0])  # First row is headers
# df.rename(columns={"P1_001N": "Total Population"}, inplace=True)


response.status_code
