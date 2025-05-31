
# 🌲 Vancouver Parks Data Dashboard

A comprehensive, Python-powered dashboard that enables users to **access**, **visualize**, and **analyze** data about Vancouver's public parks and their facilities. Designed for city planners, environmentalists, and the public, the dashboard delivers location-based insights and facility-level analysis.

---

## 🎯 Purpose

This application provides a platform for exploring Vancouver’s parks and their facilities through:
- Searchable filters (by name, facility, washroom availability, neighborhood)
- Facility distribution visualizations
- Interactive park location maps
- Distance-to-center calculations

---

## 🗂️ Data Sources

- **Vancouver Parks Dataset**  
  [Download CSV](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B)

- **Vancouver Parks Facilities Dataset**  
  [Download CSV](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks-facilities/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B)

---

## 🏗️ Project Structure

```
final_project/
├── data_dashboard.py            # Main entry point for the dashboard
├── fetch_data.py                # Downloads and parses park/facility datasets
├── analysis_functions.py        # Analyzes data for visualization
├── data_visualization.py        # Creates graphs and charts (matplotlib, folium)
├── user_interface.py            # Handles command-line interactions
├── controller_helper.py         # Helper logic to connect UI with backend
├── park.py                      # Park class definition
├── park_facility.py             # ParkFacility class definition
├── .gitignore
└── README.md
```

---

## 🧱 Core Classes

### `Park`
Represents an individual park with attributes:
- `park_id` (str)
- `park_name` (str)
- `special_features` (str)
- `facilities` (str)
- `washrooms` (str)
- `latitude` (float)
- `longitude` (float)
- `street_location` (str)
- `neighbourhood` (str)

### `ParkFacility`
Represents a park facility type with attributes:
- `parks` (list of Park)
- `type` (str)
- `count` (int)

---

## 📊 Features

- 🔍 Search for parks by:
  - Park ID or name
  - Neighborhood
  - Facility availability
  - Special features or washrooms

- 🧮 Facility analysis:
  - Facility-to-park ratios by type
  - Total facility counts by neighborhood

- 📍 Map visualizations:
  - Parks in selected neighborhoods
  - Distance from park to neighborhood center

- 📈 Graphical output:
  - Pie charts, bar charts (matplotlib)
  - Interactive maps (folium)

---

## 🖥️ How to Run

```bash
# Clone the repo
git clone https://github.com/zyc127/vancouver-parks-data-dashboard.git
cd vancouver-parks-data-dashboard

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
python data_dashboard.py
```

---

## 🧪 Technologies Used

- `matplotlib` – for plotting charts
- `folium` – for interactive maps
- `geopy` – to calculate geographical distances
- `requests` – to fetch open datasets

---

## 🙋‍♀️ User Interaction

Users interact via a simple **command-line interface**:
- Menu-driven options
- Search and filter functionality
- Triggers data fetch, analysis, and visualization