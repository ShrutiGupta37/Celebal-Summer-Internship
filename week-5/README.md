# 🏠 House Prices - Advanced Regression Techniques

Welcome to the **House Price Prediction** project!  
This project uses advanced regression models to predict house prices based on various features from Ames Housing dataset — originally featured in a Kaggle competition.

---

## Dataset

The dataset includes detailed information on 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa.

- **Train Data**: `train.csv` – includes house features and sale prices (target)
- **Test Data**: `test.csv` – includes house features for which we predict prices

---

## Problem Statement

> Predict the final price of each house in the test dataset based on the features provided.

---

## Workflow Summary

### 1. Data Loading & Exploration
- Loaded both train and test datasets using `pandas`
- Visualized distributions, relationships, and outliers using `matplotlib` and `seaborn`

### 2. Data Cleaning & Preprocessing
- Handled missing values based on domain knowledge
- Dropped features with excessive missing values (e.g. `PoolQC`, `Fence`)
- Imputed remaining missing values using:
  - Median (for numerical features)
  - Mode or "None" (for categorical features)
- Applied **log1p transformation** on skewed numerical features
- One-hot encoded categorical variables using `pd.get_dummies()`

### 3. Train-Validation Split
- Split data into training and validation sets using `train_test_split`

### 4. Model Training
Trained and evaluated the following models:
- Linear Regression
- Ridge Regression *(best performance)*
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

### 5. Model Evaluation
Evaluated models using:
- **Root Mean Squared Error (RMSE)**
- **R² Score**

Example output:

| Model             | RMSE   | R² Score |
|------------------|--------|----------|
| Ridge Regression | 0.1237 | 0.9179   |
| Linear Regression| 0.1253 | 0.9159   |

### 6. 🏁 Final Prediction & Submission
- Ridge model was used to predict `SalePrice` on test data
- Applied `np.expm1()` to reverse the log transformation
- Saved results in `prediction.csv`

---

## 🚀 Tech Stack

| Tool / Library     | Purpose                            |
|--------------------|------------------------------------|
| `pandas`           | Data manipulation                  |
| `numpy`            | Numerical operations               |
| `matplotlib`       | Data visualization                 |
| `seaborn`          | Advanced visualization             |
| `scikit-learn`     | ML models & preprocessing          |
| `xgboost`          | Gradient boosting model            |


