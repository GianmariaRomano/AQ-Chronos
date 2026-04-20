import os
import requests
import re
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAQ_API_KEY")
HEADERS = {"X-API-Key": API_KEY}

# City list.
LOCATION_IDS = {
    "New York - Brooklyn": 6091551,
    "Manaus": 5040030,
    "London - Westminster": 159,
    "Lagos - LASWA Five Cowries Terminal": 5350409,
    "Pretoria - North Suburb": 3021125,
    "Beijing - Chunxiu Lu": 2836346,
    "Osaka - 1-chōme-5-40 Kohama": 1214942,
    "Sydney": 2392564
}

def get_all_aqi():
    rows = []
    for city, loc_id in LOCATION_IDS.items():
        try:
            # Get sensors for the current city.
            url = f"https://api.openaq.org/v3/locations/{loc_id}/sensors"
            res = requests.get(url, headers=HEADERS).json()
            s_id = next(s['id'] for s in res['results'] if s['parameter']['name'] == 'pm25')

            # Get the latest measurements for the current cities.
            m_url = f"https://api.openaq.org/v3/sensors/{s_id}/measurements"
            m_res = requests.get(m_url, headers=HEADERS, params={"limit": 1}).json()
            
            if not m_res.get('results'):
                raise ValueError("No data.")

            val = m_res['results'][0]['value']
            status = "🟢 Good" if val <= 12 else "🟡 Moderate" if val <= 35 else "🟠 Sensitive" if val <= 55 else "🔴 Unhealthy"
            rows.append(f"| {city} | {val:.2f} | {status} |")
        except:
            rows.append(f"| {city} | N/A | ⚪ Not Available |") # Fallback status.
        time.sleep(0.5)
    return rows

def update_readme(rows):
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
    
    # Build the table string.
    table_content = (
        '<div align="center">\n\n'
        '| City | PM2.5 (µg/m³) | Status |\n'
        '| :--- | :---: | :---: |\n'
    )
    table_content += "\n".join(rows)
    table_content += f"\n\n*Last Updated: {date_str}*\n\n</div>"
    
    with open("STATS.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Fix the regular expression to ensure it only modifies the table
    pattern = r".*?"
    replacement = f"\n{table_content}\n"

    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("STATS.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    if not API_KEY:
        print("❌ API Key missing")
    else:
        city_rows = get_all_aqi()
        if city_rows:
            update_readme(city_rows)
            print("✅ README updated with multi-city stats.")
