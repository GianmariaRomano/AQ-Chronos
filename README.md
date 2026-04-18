# 🍃 AQ-Chronos: Smart Air Quality Surveillance Across the Globe

Modern smart cities integrate IoT sensors and artificial intelligence to transform urban environments.

**AQ-Chronos** leverages the OpenAQ ecosystem and Facebook Prophet to provide predictive insights into global air quality, specifically focusing on PM2.5 concentrations. 

---

## 📌 Project Overview

AQ-Chronos is a data science pipeline designed to:
- **Monitor:** Fetch real-time pollutants from 8 global hubs.
- **Forecast:** Predict 72-hour AQI trends using time-series modeling.
- **Visualize:** Map localized sensor data for intuitive urban analysis.

---

## 📊 Dataset

- **Source:** [OpenAQ API V3](https://openaq.org/)
- **Modeling:** `Prophet` for additive time-series forecasting.
- **Mapping:** `Folium` for interactive geospatial visualization.

---

## 🌳 Daily Statistics
> [!IMPORTANT]
> This section updates automatically every 24 hours via GitHub Actions.

<div align="center">

| City | PM2.5 (µg/m³) | Status |
| :--- | :---: | :---: |
| *Waiting for first automated update...* | | |

</div>
---

## ⚙️ Project Pipeline

The repository follows a modular structure to ensure scalability across multiple cities:
1. **Data Ingestion**: `daily_aqi.py` fetches the latest readings for the daily summary.
2. **Analysis**: `notebooks/aq_chronos.ipynb` performs historical trend analysis and seasonality detection.
3. **Automation**: GitHub Actions triggers the daily refresh and updates this README.

---

## 📂 Project Structure

```html
<pre>
├── .github/workflows/
│   └── daily_aqi.yml                    # GitHub Actions automation workflow
├── notebooks/
│   └── aq_chronos.ipynb
├── aq_chronos_air_map.html              # Generated interactive global map
├── daily_aqi.py                         # Script for daily README updates
├── requirements.txt                     # Project dependencies
├── .env.example                         # Template for API keys
├── .gitignore                           # Prevents sensitive keys from being pushed
├── LICENSE
└── README.md
</pre>
```

---

## 🚀 Running the Project

Follow these steps to set up the global air quality surveillance system on your local machine.

### 1. Prerequisites
- **Python 3.10+** installed on your system.
- An **OpenAQ API Key**. You can obtain one for free by creating an account at [explore.openaq.org](https://explore.openaq.org/).

### 2. Installation & Setup
```bash
# Clone the repository
git clone [https://github.com/yourusername/AQ-Chronos.git](https://github.com/yourusername/AQ-Chronos.git)
cd AQ-Chronos

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a ```.env``` file in the root directory by copying the example template:
```bash
cp .env.example .env
```
Open the ```.env``` file and insert your OpenAQ API key:
```bash
OPENAQ_API_KEY=your_actual_api_key_here
```
### 4. Execution
Open ```notebooks/aq_chronos.ipynb``` in Jupyter to run the Prophet forecasting model, generate the ```aq_chronos_air_map.html``` file and view diagnostics.

In particular, you can change the ```LOCATION_IDS``` dictionary in your local files to analyse the air quality patterns for other cities as well.

You can get the IDs for other cities by using the [OpenAQ Explorer](https://explore.openaq.org/#1.2/20/40) web application.

---
