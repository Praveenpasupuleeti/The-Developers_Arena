# House Price Prediction System

## Project Overview

The House Price Prediction System is an end-to-end Machine Learning application developed to predict property prices based on various housing features such as area, number of bedrooms, bathrooms, property age, location, and property type.

This project demonstrates the complete machine learning workflow including data preprocessing, feature engineering, model training, evaluation, model deployment, and prediction through a web-based interface.

---

# Business Problem

Real estate pricing is influenced by multiple factors and manual valuation can be time-consuming and inconsistent.

The objective of this project is to build an intelligent machine learning model that can accurately estimate house prices based on property characteristics, helping buyers, sellers, and real estate agencies make informed decisions.

---

# Project Objectives

* Build a complete machine learning pipeline.
* Perform data cleaning and preprocessing.
* Apply feature engineering techniques.
* Compare multiple machine learning algorithms.
* Evaluate model performance using multiple metrics.
* Deploy a prediction system through a web application.
* Save and reuse trained models.

---

# Features

✅ Data Preprocessing Pipeline

✅ Feature Engineering

✅ Multiple ML Algorithms Comparison

✅ Model Evaluation

✅ Feature Importance Analysis

✅ House Price Prediction

✅ Flask Web Application

✅ Model Persistence

✅ Error Handling and Validation

✅ Production-Ready Folder Structure

---

# Technology Stack

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Programming Language  |
| Pandas       | Data Processing       |
| NumPy        | Numerical Computation |
| Scikit-Learn | Machine Learning      |
| Flask        | Web Application       |
| Joblib       | Model Serialization   |
| Matplotlib   | Data Visualization    |
| SQLite       | Optional Data Storage |

---

# Project Structure

```text
House_Price_Prediction_System/

├── README.md
├── requirements.txt
│
├── data/
│   ├── house_prices.csv
│   ├── processed_data.csv
│   └── data_dictionary.md
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Experiments.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   ├── model_inference.py
│   └── utils.py
│
├── models/
│   ├── random_forest_model.pkl
│   ├── linear_regression_model.pkl
│   ├── decision_tree_model.pkl
│   └── model_metadata.json
│
├── app/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── tests/
│
├── docs/
│
├── config/
│
└── scripts/
```

---

# Dataset Information

Dataset Name:

house_prices.csv

Target Variable:

Price

Sample Features:

* Area (sqft)
* Bedrooms
* Bathrooms
* Property Age
* Location
* Property Type

---

# Machine Learning Workflow

## 1. Data Collection

The dataset is loaded using Pandas.

## 2. Data Cleaning

* Missing values handling
* Duplicate removal
* Data type conversion

## 3. Feature Engineering

Features created:

* Price Per Square Foot
* Property Age Category
* Location Encoding
* Property Type Encoding

## 4. Model Training

Algorithms Implemented:

### Linear Regression

Used as baseline model.

### Decision Tree Regressor

Captures nonlinear relationships.

### Random Forest Regressor

Ensemble model with improved accuracy.

---

# Model Evaluation

Evaluation Metrics:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score
* Cross Validation Score

Sample Results:

| Algorithm         | MAE      | R² Score |
| ----------------- | -------- | -------- |
| Linear Regression | ₹650,000 | 0.71     |
| Decision Tree     | ₹520,000 | 0.79     |
| Random Forest     | ₹425,000 | 0.85     |

Best Model:

Random Forest Regressor

---

# Feature Importance Analysis

Top Contributing Features:

| Feature      | Importance |
| ------------ | ---------- |
| Area         | 45%        |
| Location     | 22%        |
| Property Age | 15%        |
| Bedrooms     | 10%        |
| Bathrooms    | 8%         |

Key Insight:

Property area is the strongest predictor of house prices.

---

# Web Application

The project includes a Flask-based web interface.

Input Fields:

* Area
* Bedrooms
* Bathrooms
* Age
* Location
* Property Type

Output:

Predicted House Price

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/yourusername/house-price-prediction-system.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Train Models

```bash
python scripts/train_model.py
```

## Start Web Application

```bash
python app/app.py
```

---

# Sample Prediction

Input:

Area: 1200 sqft

Bedrooms: 3

Bathrooms: 2

Age: 5 years

Location: City Center

Property Type: Apartment

Prediction:

₹12,450,000

Confidence Interval:

₹11,205,000 – ₹13,695,000

---

# Testing

The project includes test cases for:

* Data preprocessing
* Feature engineering
* Model training
* Prediction pipeline
* Web application functionality

Run tests:

```bash
pytest
```

---

# Future Enhancements

* Deep Learning Models
* Real-Time Data Integration
* Cloud Deployment
* Model Monitoring
* User Authentication
* Interactive Dashboards
* Automated Retraining

---

# Learning Outcomes

This project demonstrates:

* Machine Learning Fundamentals
* Data Preprocessing
* Feature Engineering
* Model Selection
* Model Evaluation
* Hyperparameter Tuning
* Model Deployment
* Web Development with Flask

---

# Author

Praveen Pasupuleti

Month 4 Internship Project

Machine Learning Fundamentals

Developers Arena Internship Program

---

# License

This project is created for educational and internship submission purposes.
