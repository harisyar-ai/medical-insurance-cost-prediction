# 🩺 Medical Insurance Cost Prediction 
### Machine Learning-Based Health Insurance Cost Estimator

<div align="center">
  <img src="https://raw.githubusercontent.com/harisyar-ai/medical-insurance-cost-prediction/main/profile_img.png" alt="Medical Insurance Cost Predictor" width="95%">
</div>

<div align="center">

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## Project Overview

The **Medical Insurance Cost Prediction** project is a machine learning application designed to **estimate annual health insurance costs** based on demographic and health-related features.  

The model is trained on real-world medical insurance data and includes **extensive feature engineering**, combining numerical, categorical, polynomial, and interaction features to maximize prediction accuracy.  

This project is ideal for:  

- Individuals wanting to estimate health insurance costs,  
- Students and developers learning regression and feature engineering,  
- Professionals exploring real-world applications of ML pipelines and Streamlit deployment.  

---

## Why This Project Matters

Health insurance costs are often opaque and vary widely depending on age, BMI, smoking status, region, and family history. Most individuals struggle to estimate their expected charges or understand the factors driving costs.  

This project addresses that gap by providing a **fast, explainable, and interactive ML-based estimator**, helping users make informed decisions about insurance planning.  

**Key benefits**:  
- Accurate cost estimation without complex formulas or actuarial knowledge,  
- Interactive exploration of feature impacts on insurance cost,  
- Hands-on example of **feature engineering and regression modeling**,  
- Useful for both educational purposes and practical cost planning.  

**Who benefits**:  
- Policy seekers estimating insurance premiums,  
- Students learning regression models, pipelines, and feature engineering,  
- Developers building predictive analytics apps,  
- Health planners and analysts exploring data-driven insights.  

---

## Live Web App

<div style="padding:10px; font-size:100%; text-align:left;">
    URL: 
    <a href="https://your-app-link.streamlit.app/" target="_blank">
        Click here to open the Medical Insurance Cost Predictor
    </a>
</div>

---

## Dataset Overview — Medical Insurance Dataset

This project uses the **Medical Cost Personal Dataset** from Kaggle, which includes demographic and health metrics relevant to insurance charges.  

### **Entries**
- 1,338 individual records

### **Columns**

| Column       | Description                                   |
|--------------|-----------------------------------------------|
| age          | Age of the individual                          |
| sex          | Gender of the individual                        |
| bmi          | Body Mass Index                                |
| children     | Number of children                              |
| smoker       | Smoker status (yes/no)                          |
| region       | Residential region                             |
| charges      | Annual medical insurance charges (target)      |

### **Dataset Details**
- Format: CSV  
- Size: ~10 KB  
- License: Public dataset on Kaggle

**Dataset Link**:  
<div style="padding:10px; font-size:100%; text-align:left;">
    <a href="https://www.kaggle.com/datasets/mirichoi0218/insurance" target="_blank">
        Click here for the Medical Insurance Dataset
    </a>
</div>

---

## Repository Structure
```text
.
📁 Medical_Insurance_Cost_Prediction/
├── profile_img.png                 ← Project banner
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── data/
│   ├── Raw/
│   │   └── insurance.csv          ← Raw Dataset
│   └── Processed/
│       └── cleaned_dataset.csv    ← Cleaned Dataset
│   └── Report/
│       └── Medical_Insurance_Cost_Prediction.html ← Summary Report of the Dataset
├── src/
│   ├── file.ipynb                 ← Main programming file (preprocessing & training)
├── models/
│   └── model.pkl                   ← Random Forest pkl file
└── app/
    └── app.py                      ← Interactive Streamlit web app
````

---

## How Features Are Processed

1. **Data Cleaning & Preprocessing**

   * Remove duplicates, handle missing values
   * Stratified train-test split to maintain smoker ratio

2. **Feature Engineering**

   * Binary smoker variable
   * Polynomial & interaction features (age², bmi², age*bmi, smoker*bmi, etc.)
   * Binning features: age groups & BMI categories
   * Boolean flags like `has_children`

3. **Encoding & Transformation**

   * One-hot encoding for categorical features (`sex`, `region`, `bmi_category`, `age_group`)
   * Ordinal encoding for smoker
   * Log transformation on `charges` for better regression performance

4. **Pipeline Construction**

   * Combined preprocessing + model in a `Pipeline` for reproducibility and deployment

5. **Model Selection & Training**

   * Tested multiple regressors: Linear, Ridge, Lasso, ElasticNet, DecisionTree, ExtraTrees, GradientBoosting, AdaBoost, SVR, KNN, MLP, LightGBM, CatBoost, XGBoost, RandomForest
   * Performance on Test Set :
     | Model            | R² Score | MAE       | RMSE      |
     | ---------------- | -------- | --------- | --------- |
     | RandomForest     | 0.9246   | 1,536.05  | 3,296.82  |
     | KNN              | 0.9051   | 1,983.19  | 3,697.76  |
     | AdaBoost         | 0.8957   | 3,016.66  | 3,877.30  |
     | LightGBM         | 0.8885   | 2,348.80  | 4,008.53  |
     | CatBoost         | 0.8871   | 2,179.42  | 4,033.65  |
     | GradientBoosting | 0.8842   | 2,124.93  | 4,085.34  |
     | ExtraTrees       | 0.8819   | 2,105.95  | 4,126.54  |
     | LinearRegression | 0.8766   | 2,279.57  | 4,217.06  |
     | Ridge            | 0.8735   | 2,285.33  | 4,269.66  |
     | SVR              | 0.8540   | 2,091.48  | 4,587.51  |
     | XGBoost          | 0.8210   | 2,786.57  | 5,079.80  |
     | ElasticNet       | 0.7999   | 2,868.48  | 5,371.01  |
     | DecisionTree     | 0.7826   | 2,494.58  | 5,598.67  |
     | Lasso            | 0.6252   | 3,691.84  | 7,350.03  |
     | MLP              | -64.2322 | 28,354.34 | 96,972.10 |

   * Random Forest was selected as the final model based on highest R² score and lowest MAE/RMSE,
     making it the most accurate and robust model for predicting medical insurance costs.
   


---

## Run Locally

```bash
git clone https://github.com/harisyar-ai/medical-insurance-cost-prediction.git
cd medical-insurance-cost-prediction
pip install -r requirements.txt
streamlit run app/app.py
```

---

## Future Improvements

* Integrate SHAP/LIME for feature importance visualization
* Add more advanced ML models (e.g., XGBoost or ensemble stacking)
* Include real-time cost comparison based on region and age group
* Add historical or trend-based insurance analysis

---


---

* ```
            Developed by Haider • Shehzad • Haris
                         February 2026
          Stars & feedback are highly appreciated ⭐
                   github.com/harisyar-ai
  ```
