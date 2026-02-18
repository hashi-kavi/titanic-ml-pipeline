🚢 Titanic: End-to-End Data Engineering & ML Pipeline

This project demonstrates a production-grade machine learning workflow. Beyond simple prediction, it focuses on modular pipeline architecture, stratified validation, and feature importance analysis to ensure the model generalizes effectively to unseen data.

🏗️ The Engineering Pipeline

The project uses a custom TitanicDataPipeline class for data cleaning and a Scikit-Learn ColumnTransformer + Pipeline architecture for model training. This design prevents data leakage and ensures consistent preprocessing across training and evaluation stages.

🔧 Key Technical Features

Production-Grade Pipelines
Combined StandardScaler and ColumnTransformer into a unified Pipeline object to automatically scale numerical features while passing categorical features through appropriately.

Stratified Cross-Validation
Implemented StratifiedKFold (5 splits) to preserve the original class distribution in each fold, ensuring stable and reliable performance evaluation.

Advanced Feature Engineering

FamilySize: Engineered from SibSp + Parch + 1

IsAlone: Derived binary indicator based on FamilySize

Multicollinearity Management
Analyzed feature correlations and removed redundant high-correlation features to reduce noise and improve model stability.

Dummy Variable Handling
Applied drop_first=True during One-Hot Encoding to avoid the Dummy Variable Trap and reduce unnecessary dimensionality.

📊 Model Performance & Evaluation

Multiple models were benchmarked using both hold-out testing and 5-Fold Stratified Cross-Validation. Mean Accuracy and Standard Deviation were used to evaluate both performance and stability.

🏆 Leaderboard (5-Fold Stratified CV)
Model	Train Acc	Test Acc	Mean CV Accuracy
XGBoost	~85%	~83%	~82.5%
Random Forest	~83%	~82%	~81.8%
SVM	~82%	~81%	~80.9%
Logistic Regression	~80%	~79%	~79.2%
📈 Feature Importance & Error Analysis

Using the RandomForestClassifier feature importance scores, the model identified the most influential survival predictors:

Sex

Pclass

Fare

Confusion matrices were generated to analyze True Positives, False Positives, False Negatives, and True Negatives, ensuring balanced classification performance beyond simple accuracy metrics.

📁 Project Structure
TITANIC/
│
├── data/
│   ├── Titanic-Dataset.csv       # Raw Data
│   └── cleaned_titanicdata.csv   # Model-Ready Feature Matrix
│
├── notebooks/
│   └── EDA_Visuals.ipynb         # EDA, Benchmarking & Cross-Validation
│
├── scripts/
│   └── titanic_cleaner.py        # Object-Oriented Preprocessing Class
│
└── README.md

🚀 How to Run
Clone the Repository
git clone https://github.com/hashi-kavi/titanic-ml-pipeline.git

Execute the Preprocessing Script
python scripts/titanic_cleaner.py

Explore the Analysis

Open:

notebooks/EDA_Visuals.ipynb


to view model comparison, cross-validation results, confusion matrices, and feature importance visualizations.

👨‍🔬 Author

Kavindya Ranaweera
Aspiring AI/ML Engineer

Interests:
MLOps | Data Engineering | Reinforcement Learning

If you want, I can also give you:

🔥 A stronger, internship-optimized version

📌 A LinkedIn post version

🌍 A portfolio showcase version

🧠 A “world-class AI engineer” upgraded README

Just tell me which one you want next 👑

no i want in a copy paste mode note in chat

Got it 👍
Here is your fully cleaned, properly spaced, plain text version — no markdown formatting, no tables — just ready to copy and paste directly into a text editor.

🚢 Titanic: End-to-End Data Engineering & ML Pipeline

This project demonstrates a production-grade machine learning workflow. Beyond simple prediction, it focuses on modular pipeline architecture, stratified validation, and feature importance analysis to ensure the model generalizes effectively to unseen data.

────────────────────────────────────────

🏗️ The Engineering Pipeline

The project uses a custom TitanicDataPipeline class for data cleaning and a Scikit-Learn ColumnTransformer + Pipeline architecture for model training. This design prevents data leakage and ensures consistent preprocessing across training and evaluation stages.

Key Technical Features:

Production-Grade Pipelines:
Combined StandardScaler and ColumnTransformer into a unified Pipeline object to automatically scale numerical features while passing categorical features appropriately.

Stratified Cross-Validation:
Implemented StratifiedKFold (5 splits) to preserve the original class distribution in each fold, ensuring stable and reliable performance evaluation.

Advanced Feature Engineering:

FamilySize: Engineered from SibSp + Parch + 1

IsAlone: Derived binary indicator based on FamilySize

Multicollinearity Management:
Analyzed feature correlations and removed redundant high-correlation features to reduce noise and improve model stability.

Dummy Variable Handling:
Applied drop_first=True during One-Hot Encoding to avoid the Dummy Variable Trap and reduce unnecessary dimensionality.

────────────────────────────────────────

📊 Model Performance & Evaluation

Multiple models were benchmarked using both hold-out testing and 5-Fold Stratified Cross-Validation. Mean Accuracy and Standard Deviation were used to evaluate both performance and stability.

Leaderboard (5-Fold Stratified Cross-Validation):

XGBoost
Train Accuracy: ~85%
Test Accuracy: ~83%
Mean CV Accuracy: ~82.5%

Random Forest
Train Accuracy: ~83%
Test Accuracy: ~82%
Mean CV Accuracy: ~81.8%

SVM
Train Accuracy: ~82%
Test Accuracy: ~81%
Mean CV Accuracy: ~80.9%

Logistic Regression
Train Accuracy: ~80%
Test Accuracy: ~79%
Mean CV Accuracy: ~79.2%

────────────────────────────────────────

📈 Feature Importance & Error Analysis

Using the RandomForestClassifier feature importance scores, the model identified the most influential survival predictors:

Sex

Pclass

Fare

Confusion matrices were generated to analyze True Positives, False Positives, False Negatives, and True Negatives, ensuring balanced classification performance beyond simple accuracy metrics.

────────────────────────────────────────

📁 Project Structure

TITANIC/

data/
Titanic-Dataset.csv (Raw Data)
cleaned_titanicdata.csv (Model-Ready Feature Matrix)

notebooks/
EDA_Visuals.ipynb (EDA, Benchmarking & Cross-Validation)

scripts/
titanic_cleaner.py (Object-Oriented Preprocessing Class)

README.md

────────────────────────────────────────

🚀 How to Run

Clone the repository:

git clone https://github.com/hashi-kavi/titanic-ml-pipeline.git

Execute the preprocessing script:

python scripts/titanic_cleaner.py

Explore the analysis:

Open notebooks/EDA_Visuals.ipynb to view model comparison, cross-validation results, confusion matrices, and feature importance visualizations.

────────────────────────────────────────

👨‍🔬 Author

Kavindya Ranaweera
Aspiring AI/ML Engineer

Interests:
MLOps
Data Engineering
Reinforcement Learning

────────────────────────────────────────