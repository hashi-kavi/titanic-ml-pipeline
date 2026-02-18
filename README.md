# 🚢 Titanic Data Engineering Pipeline

A professional Python-based pipeline that cleans, engineers, and prepares the Titanic dataset for Machine Learning models.

## 🛠️ Features
- **Automated Imputation:** Fills missing 'Age' values using the median of each 'Pclass' to maintain demographic accuracy.
- **Categorical Encoding:** Converts 'Sex' and 'Embarked' into numerical/boolean formats using Mapping and One-Hot Encoding.
- **Feature Engineering:** - `FamilySize`: Combined `SibSp` and `Parch`.
    - `IsAlone`: Binary feature to capture social dynamics.
- **Data Reduction:** Dropped high-cardinality features (`Name`, `Ticket`, `PassengerId`) and high-null features (`Cabin`).

## 📁 Project Structure
- `data/`: Contains raw and cleaned CSV files.
- `scripts/`: Production-ready Python class (`titanic_cleaner.py`).
- `notebooks/`: Exploratory Data Analysis and visualizations.

## 🚀 How to Run
```bash
python scripts/titanic_cleaner.py