import bs4 as bs
import requests
import pandas as pd

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = bs.BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]


short_description = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temperature = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
full_description = [d["title"] for d in seven_day.select(".tombstone-container img")]

temperature.append('no data yet')

# print(len(periods))
# print(len(short_descs))
# print(len(temps))
# print(len(descs))
print('WEATHER IN SAN-FRAN')


weather = pd.DataFrame({
        "PERIOD": periods,
        "SHORT_DESCRIPTION": short_description,
        "TEMPERATURE": temperature,
        "FULL_DESCRIPTION": full_description
    })

print(weather)