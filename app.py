import requests
from bs4 import BeautifulSoup
import json
from fastapi import FastAPI

#importing libraries




app=FastAPI()
# initializing fastAPI


@app.get('/{id}')
def get_weather_forecast(id):

    # url for requesting
    url=f"https://city.imd.gov.in/citywx/city_weather_test.php?id={id}"
    response=requests.get(url)

    soup=BeautifulSoup(response.content,'html5lib')

    properties={
        'cellpadding':0,
        'cellspacing':0,
        'width':'100%',
    }
    raw_data=soup.find_all('table',properties)

    if len(raw_data)<2:
        return {'message':"internal server error"}
    
    # Selecting the second table
    data =raw_data[1]
    # return json(data)
    # reteriveing all the rows
    rows=data.find_all('tr')
    # return rows_wise_data
    forecast_data = []

# Loop through each row to extract data
    for row in rows:
        cols = row.find_all('td')
    
    # Check if the row has enough columns (in case of malformed rows)
        if len(cols) >= 5:
            date = cols[0].text.strip()
            try:
                minT = float(cols[1].text.strip())
                maxT = float(cols[2].text.strip())
            except ValueError:
                minT = maxT = None  # Handle invalid temperature data
            desc = cols[4].text.strip()
        
        # Append the data for each row as a dictionary
            forecast_data.append({
                "Date": date,
                "Minimum Temperature": minT,
                "Maximum Temperature": maxT,
                "Weather Description": desc
            })
    print(forecast_data)
    return forecast_data

