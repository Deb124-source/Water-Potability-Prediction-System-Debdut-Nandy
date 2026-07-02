# AquaSense AI – Water Potability Prediction System

## Overview

AquaSense AI is a machine learning web application that predicts whether water is safe for drinking based on various physicochemical properties. The project combines data preprocessing, XGBoost classification, and an interactive Streamlit interface to provide instant water potability predictions.

## Live Demo
https://water-potability-prediction-system-debdut-nandy.streamlit.app/

## Features

- Predicts whether water is drinkable or not
- Interactive Streamlit web application
- Built using the XGBoost Classifier
- Handles missing values using median imputation during training
- Displays prediction confidence
- Clean and user-friendly interface

## Dataset

The project uses the **Water Potability Dataset**, which contains water quality measurements and a target variable indicating whether the water is safe for drinking.

### Input Features

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

### Target

- 0 – Not Drinkable
- 1 – Drinkable

## Machine Learning Workflow

- Data Cleaning
- Missing Value Imputation
- Train-Test Split
- XGBoost Classifier Training
- Model Evaluation
- Model Serialization using Joblib
- Streamlit Deployment

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Streamlit

## Project Structure

```
AquaSense-AI/
│
├── app.py
├── water_quality_model.pkl
├── features.json
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AquaSense-AI.git
```

Navigate to the project directory:

```bash
cd AquaSense-AI
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Model Performance

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Since the Water Potability dataset is naturally imbalanced and contains overlapping feature distributions, evaluation focuses on multiple classification metrics rather than accuracy alone.

## Future Improvements

- Hyperparameter tuning
- Cross-validation
- Probability visualization
- Water Quality Index (WQI) integration
- Explainable AI using SHAP values
- Cloud deployment enhancements

## License

This project is intended for educational and portfolio purposes.
