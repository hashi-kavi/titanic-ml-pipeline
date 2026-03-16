# Titanic Survival Predictor App

This folder contains a Streamlit application that predicts whether a passenger on the Titanic would have survived. The app uses a pre-trained Random Forest model and turns a few passenger details into a real-time prediction with confidence.

## Overview

The app is designed as a lightweight inference interface for the Titanic machine learning project. It loads the saved model, accepts passenger inputs from the browser, engineers the required features, and returns a survival prediction instantly.

## Features

- Interactive Streamlit interface for passenger inputs
- Pre-trained Random Forest model for local prediction
- Automatic feature engineering before inference
- Probability-based output for clearer interpretation
- Model loading based on the app file location, not the terminal location

## Folder Contents

- `app.py` - Streamlit application code
- `models/titanic_rf_model.pkl` - Serialized trained model
- `README.md` - Documentation for this app

## Tech Stack

- Python
- Streamlit
- pandas
- joblib
- scikit-learn

## Requirements

Use Python 3.x and install the following packages:

- streamlit
- pandas
- numpy
- joblib
- scikit-learn

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

## Run The App

You can run the app either from this folder or from the project root.

From inside `titanic_app`:

```powershell
streamlit run app.py
```

From the project root:

```powershell
streamlit run titanic_app/app.py
```

After launch, Streamlit will provide a local URL, usually `http://localhost:8501`.

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

The app derives some values automatically before sending them to the model:

- `Sex`: male = 0, female = 1
- `FamilySize`: `SibSp + Parch + 1`
- `IsAlone`: `1` if `FamilySize == 1`, otherwise `0`
- `Embarked_Q`: `1` if the embarkation port is `Q`, otherwise `0`
- `Embarked_S`: `1` if the embarkation port is `S`, otherwise `0`

If both `Embarked_Q` and `Embarked_S` are `0`, the passenger is treated as having embarked from `C`.

## Output

- If the model predicts `1`, the app displays `Survived` with survival probability.
- If the model predicts `0`, the app displays `Perished` with the corresponding probability.

## Example Use

Enter passenger details such as class, sex, age, fare, family counts, and embarkation port, then click `Predict Survival`. The app returns both the predicted outcome and the model confidence.

## Screenshot

To show the app UI on GitHub, save a screenshot image in this location:

```text
titanic_app/
  assets/
    titanic-app-screenshot.png
```

After you add the image file, GitHub will render it automatically using the line below:

![Titanic Survival Predictor App](./assets/titanic-app-screenshot.png)

If you use a different file name, update the path in the Markdown image link.

## Troubleshooting

- Model file not found:
  - Confirm `models/titanic_rf_model.pkl` exists.
- Missing package error:
  - Activate the virtual environment and reinstall dependencies.
- Streamlit command not recognized:
  - Run `pip install streamlit` inside the active environment.
