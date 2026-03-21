# 🚢 Titanic Survival Predictor (Machine Learning Web App)

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![ML](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)

## Live Demo

Try the app here:
https://titanic-ml-pipeline-rgn69hxdfjclsjyulfyhkh.streamlit.app/

---

## Overview

This project is a **Streamlit-based machine learning web application** that predicts whether a passenger on the Titanic would have survived.

It uses a **pre-trained Random Forest model** and transforms user inputs into real-time predictions with confidence scores.

---

## Screenshot

![Titanic Survival Predictor App](./assets/image.png)

---

## Features

* Real-time ML predictions through an interactive UI
* Automated feature engineering pipeline
* Probability-based predictions for better interpretability
* Lightweight and fast local inference
* Model loading independent of terminal location

---

## How It Works (Pipeline)

1. User inputs passenger details via Streamlit UI
2. App performs feature engineering
3. Pre-trained Random Forest model is loaded
4. Model predicts survival probability
5. Result is displayed with confidence score

---

## Model Details

* Algorithm: Random Forest Classifier
* Trained on: Titanic dataset
* Features: Engineered from raw passenger data
* Output: Binary classification with probability

---

## Purpose

This project demonstrates:

* End-to-end ML deployment
* Feature engineering for real-world data
* Model inference in a web application
* Clean and user-friendly UI design

---

## Tech Stack

* Python
* Streamlit
* pandas
* numpy
* joblib
* scikit-learn

---

## Requirements

Use Python 3.8+ and install the following packages:

* streamlit
* pandas
* numpy
* joblib
* scikit-learn

---

## Setup

In Windows PowerShell:

1. Create a virtual environment:

```powershell
python -m venv .venv
```

2. Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install streamlit pandas numpy joblib scikit-learn
```

---

## Run The App

From inside `titanic_app`:

```powershell
streamlit run app.py
```

From the project root:

```powershell
streamlit run titanic_app/app.py
```

After launch, Streamlit will provide a local URL (usually http://localhost:8501).

---

## How The Prediction Works

The model expects these features:

1. `Pclass`
2. `Sex`
3. `Age`
4. `Fare`
5. `FamilySize`
6. `IsAlone`
7. `Embarked_Q`
8. `Embarked_S`

### Feature Engineering Logic

* `Sex`: male = 0, female = 1
* `FamilySize`: `SibSp + Parch + 1`
* `IsAlone`: `1` if `FamilySize == 1`, otherwise `0`
* `Embarked_Q`: `1` if port = Q
* `Embarked_S`: `1` if port = S

If both `Embarked_Q` and `Embarked_S` are `0`, the passenger is treated as embarking from `C`.

---

## Output

* `1` → **Survived** (with probability)
* `0` → **Perished** (with probability)

---

## Folder Structure

```
titanic_app/
│── app.py
│── models/
│   └── titanic_rf_model.pkl
│── assets/
│   └── image.png
│── README.md
```

---

## Troubleshooting

* Model file not found:
  Ensure `models/titanic_rf_model.pkl` exists

* Missing packages:
  Activate virtual environment and reinstall dependencies

* Streamlit not recognized:
  Run `pip install streamlit`

---

## Note

The virtual environment (`.venv`) is excluded using `.gitignore`.

---
