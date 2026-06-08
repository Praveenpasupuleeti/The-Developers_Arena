# Weather Data Pipeline System

## Overview

The Weather Data Pipeline System is a Python-based ETL (Extract, Transform, Load) application that collects real-time weather information from the OpenWeatherMap API, validates and processes the data, stores it in a SQLite database, and generates reports for weather analysis.

This project demonstrates core concepts of Database Management, API Integration, Data Engineering, ETL Workflows, Data Validation, Logging, and Reporting.

---

## Project Objectives

* Extract weather data from OpenWeatherMap API.
* Transform and validate incoming data.
* Load processed data into a SQLite database.
* Generate weather reports.
* Maintain logs for monitoring and debugging.
* Store historical weather records for future analysis.

---

## Features

✅ OpenWeatherMap API Integration

✅ SQLite Database Management

✅ ETL Pipeline Implementation

✅ Data Validation and Quality Checks

✅ Logging and Monitoring

✅ Historical Weather Data Storage

✅ Automated Report Generation

✅ Error Handling

✅ Modular Project Structure

---

## Technology Stack

| Technology         | Purpose                |
| ------------------ | ---------------------- |
| Python             | Core Programming       |
| SQLite             | Database               |
| OpenWeatherMap API | Weather Data Source    |
| Requests           | API Communication      |
| Pandas             | Data Processing        |
| Logging            | Monitoring & Debugging |

---

## Project Structure

```text
Weather_Data_Pipeline_System/
│
├── README.md
├── requirements.txt
│
├── config/
│   └── config.py
│
├── src/
│   ├── main.py
│   ├── database.py
│   ├── api_client.py
│   ├── etl_pipeline.py
│   ├── validators.py
│   ├── reporter.py
│   └── monitor.py
│
├── database/
│   ├── schema.sql
│   └── weather_data.db
│
├── tests/
│   └── test_pipeline.py
│
├── docs/
│   └── System_Documentation.md
│
├── reports/
│   └── sample_weather_report.txt
│
└── logs/
    └── weather_pipeline.log
```

---

## Database Schema

### Cities Table

Stores city information.

| Field     | Type    |
| --------- | ------- |
| city_id   | INTEGER |
| city_name | TEXT    |
| country   | TEXT    |
| latitude  | REAL    |
| longitude | REAL    |

### Weather Data Table

Stores weather records.

| Field             | Type     |
| ----------------- | -------- |
| record_id         | INTEGER  |
| city_id           | INTEGER  |
| temperature       | REAL     |
| humidity          | INTEGER  |
| pressure          | REAL     |
| wind_speed        | REAL     |
| weather_condition | TEXT     |
| timestamp         | DATETIME |

### Pipeline Logs Table

Stores ETL execution logs.

| Field      | Type     |
| ---------- | -------- |
| log_id     | INTEGER  |
| status     | TEXT     |
| message    | TEXT     |
| created_at | DATETIME |

---

## ETL Workflow

### 1. Extract

Weather data is fetched from OpenWeatherMap API.

### 2. Transform

Data is cleaned and validated.

Validation includes:

* Temperature validation
* Humidity validation
* Pressure validation
* Missing value checks
* Timestamp verification

### 3. Load

Validated data is inserted into the SQLite database.

---

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/weather-data-pipeline-system.git
```

### Step 2: Navigate to Project Folder

```bash
cd weather-data-pipeline-system
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure API Key

Open:

```python
config/config.py
```

Add your OpenWeatherMap API Key:

```python
API_KEY = "YOUR_API_KEY"
```

### Step 5: Run Application

```bash
python src/main.py
```

---

## Sample Output

```text
===================================
WEATHER DATA PIPELINE SYSTEM
===================================

City: Vijayawada

Temperature : 34.5 °C
Humidity    : 65 %
Pressure    : 1008 hPa
Wind Speed  : 4.2 m/s
Condition   : Clear Sky

Data Loaded Successfully

Records Stored : 1

Report Generated Successfully
```

---

## Testing

Run tests using:

```bash
python -m pytest
```

Test Coverage:

* API Integration
* Database Operations
* Data Validation
* ETL Pipeline Execution
* Report Generation

---

## Logging

Log File Location:

```text
logs/weather_pipeline.log
```

Logs include:

* API requests
* Database operations
* Validation failures
* Runtime exceptions

---

## Future Enhancements

* Multi-City Tracking
* Weather Forecast Support
* Automated Scheduling
* Dashboard Visualization
* Email Alerts
* Cloud Database Integration
* Machine Learning Weather Predictions

---

## Learning Outcomes

Through this project, the following concepts were implemented:

* SQL Fundamentals
* Database Design
* API Integration
* ETL Pipeline Development
* Data Validation
* Data Engineering Basics
* Reporting Systems
* Error Handling
* Logging and Monitoring

---

## Author

Praveen Pasupuleti

Month 3 Internship Project

Database Management & APIs

Developers Arena Internship Program

---

## License

This project is developed for educational and internship submission purposes.
