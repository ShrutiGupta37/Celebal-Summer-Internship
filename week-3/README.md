# Titanic Survival Data Analysis

This project explores the Titanic dataset using Python's data analysis and visualization libraries. The analysis focuses on identifying key factors that influenced passenger survival, such as socioeconomic status, gender, age, family size, and class.

## 📌 Dataset

The Titanic dataset used in this project is provided by the Seaborn library (`sns.load_dataset("titanic")`). It includes demographic, ticket, and survival information for passengers aboard the RMS Titanic.

## 🔍 Project Objectives

- Clean the dataset by handling missing values
- Impute missing age values using a machine learning model (Random Forest Regressor)
- Explore patterns and relationships affecting survival rates
- Visualize insights using Seaborn and Matplotlib

## 📊 Key Analysis Sections

### 1. Data Cleaning
- Removed unnecessary or highly incomplete columns (`deck`)
- Imputed missing `age` values using Random Forest Regressor
- Dropped rows with missing `embarked` or `embark_town`

### 2. Socioeconomic Insights
- 1st class passengers had much higher survival rates compared to 2nd or 3rd class
- Higher ticket fares correlated with increased survival, reflecting the advantages of wealthier passengers

### 3. Family and Social Connections
- Small families (1–3 members) had better survival rates
- Large families (5+ members) were less likely to survive
- Passengers traveling alone had lower survival rates

### 4. Age and Gender Insights
- Females had significantly higher survival rates across all classes
- Children had higher survival rates than adults, especially in 1st and 2nd class

### 5. Correlation Analysis
- Positive correlation between `fare` and `survived`
- Slight negative correlation between `pclass` and `survived`, confirming that lower classes had reduced survival rates

## 📈 Libraries Used

- pandas
- seaborn
- matplotlib
- scikit-learn

## 📝 Final Observations

- **Survival Trends:** Heavily influenced by gender, age, class, and embarkation point
- **Disparities:** Gender and class were the strongest predictors of survival
- **Data Completeness:** Imputation strategies improved the dataset's integrity for analysis

## 🚀 How to Run

1. Clone the repository
2. Open `Titanic_dataset_visualization.ipynb` in Jupyter Notebook
3. Run the notebook cells sequentially


