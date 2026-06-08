Customer Sentiment Analysis System
Project Overview

The Customer Sentiment Analysis System is a Deep Learning-based Natural Language Processing (NLP) application designed to automatically classify customer reviews into Positive, Neutral, or Negative sentiment categories.

The project demonstrates an end-to-end machine learning workflow including text preprocessing, neural network development, model training, evaluation, API deployment, Docker containerization, monitoring, and production-ready implementation.

This project was developed as part of the Month 5 – Advanced Topics & Specialization Internship Program.

Problem Statement

Organizations receive thousands of customer reviews, feedback messages, and support comments daily. Manually analyzing these reviews is time-consuming and inefficient.

The objective of this project is to automate sentiment detection using Deep Learning techniques, enabling businesses to understand customer opinions and improve products and services.

Project Objectives
Build a complete NLP preprocessing pipeline.
Develop a Deep Learning sentiment classification model.
Perform model evaluation and performance analysis.
Deploy the model through a FastAPI service.
Containerize the application using Docker.
Implement monitoring and logging mechanisms.
Create a scalable and production-ready architecture.
Features

✅ Text Cleaning and Preprocessing

✅ Tokenization and Sequence Padding

✅ Deep Learning Sentiment Classification

✅ Bidirectional LSTM Neural Network

✅ FastAPI-Based Prediction Service

✅ Docker Containerization

✅ Monitoring and Logging

✅ Error Handling and Input Validation

✅ Production-Ready Code Structure

✅ Automated Testing Framework

Technology Stack
Technology	Purpose
Python	Programming Language
TensorFlow	Deep Learning
Keras	Neural Network Development
Pandas	Data Processing
NumPy	Numerical Computing
Scikit-Learn	Evaluation Metrics
FastAPI	API Development
Uvicorn	API Server
Docker	Containerization
Pytest	Testing
Project Structure
Customer_Sentiment_Analysis_System/

├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml

├── data/
├── notebooks/
├── src/
├── models/
├── api/
├── deployment/
├── monitoring/
├── tests/
├── docs/
└── scripts/
Dataset Information

Dataset Type:

Customer Reviews Dataset

Target Classes:

Label	Sentiment
0	Negative
1	Neutral
2	Positive

Example Records:

Review	Sentiment
Great product, highly recommended.	Positive
Average quality, acceptable.	Neutral
Worst experience ever.	Negative
NLP Pipeline
Step 1: Text Cleaning

Operations performed:

Lowercasing
Punctuation removal
Special character removal
Stopword removal
Whitespace normalization
Step 2: Tokenization

Customer reviews are converted into tokens using TensorFlow Tokenizer.

Example:

Original:
Great product and amazing quality

Tokenized:
[15, 98, 45, 123]
Step 3: Sequence Padding

All review sequences are padded to a fixed length.

pad_sequences(maxlen=100)
Deep Learning Architecture
Input Review

↓

Embedding Layer

↓

Bidirectional LSTM (64 Units)

↓

Dropout Layer (0.5)

↓

Bidirectional LSTM (32 Units)

↓

Dense Layer (24 Units)

↓

Softmax Output Layer

↓

Sentiment Prediction
Model Training

Training Configuration:

Parameter	Value
Epochs	10
Batch Size	32
Optimizer	Adam
Loss Function	Sparse Categorical Crossentropy
Validation Split	20%
Model Performance
Training Results
Metric	Value
Training Accuracy	92.5%
Validation Accuracy	88.3%
Precision	87%
Recall	88%
F1 Score	87.5%
Sample Predictions
Review 1
Great product! Highly recommend.

Prediction:

Positive
Confidence: 98%
Review 2
Average quality and okay performance.

Prediction:

Neutral
Confidence: 85%
Review 3
Worst purchase of my life.

Prediction:

Negative
Confidence: 96%
API Endpoints
Predict Sentiment
POST /predict

Request:

{
  "text": "This product is amazing"
}

Response:

{
  "sentiment": "Positive",
  "confidence": 0.98
}
Batch Prediction
POST /batch_predict
Health Check
GET /health
Metrics Endpoint
GET /metrics
Docker Deployment
Build Docker Image
docker build -t sentiment-analysis .
Run Container
docker run -p 8000:8000 sentiment-analysis
Docker Compose
docker-compose up --build
Monitoring Features

The application tracks:

Total Requests
Average Response Time
Error Rate
Memory Usage
CPU Usage
Model Performance Metrics
Testing

The project contains automated tests for:

Data preprocessing
Tokenization
Model prediction
API functionality
Error handling

Run tests:

pytest
Business Impact

This system helps organizations:

Automate customer feedback analysis.
Detect negative reviews quickly.
Improve customer satisfaction.
Generate product improvement insights.
Support marketing and customer success teams.

Expected Benefits:

85% reduction in manual review effort.
Faster customer issue detection.
Improved business decision-making.
Future Enhancements
BERT-based Sentiment Analysis
Multilingual Support
Real-Time Streaming Predictions
Cloud Deployment
Kubernetes Integration
Model Drift Detection
Dashboard Visualization
Learning Outcomes

This project demonstrates:

Natural Language Processing
Deep Learning Fundamentals
Neural Network Design
Model Evaluation
API Development
Docker Containerization
Monitoring and Logging
Production Deployment
Author

Praveen Pasupuleti

Month 5 Internship Project

Advanced Topics & Specialization

Developers Arena Internship Program