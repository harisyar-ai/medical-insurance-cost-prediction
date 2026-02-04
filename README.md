# 🩺 Medical Insurance Cost Prediction 2026
### AI-Powered Prediction Using Random Forest & Feature Engineering

<div align="center" style="margin-bottom:20px;">
  <img src="-profile_img.png" alt="Medical Insurance Cost Predictor" width="95%">
</div>

<div align="center">
  <span style="background-color:#F5F5F5; padding:5px 10px; border-radius:8px;">
    <a href="https://python.org" target="_blank">
      <img src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python" alt="Python 3.11+">
    </a>
    <a href="https://scikit-learn.org" target="_blank">
      <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn" alt="Scikit-Learn">
    </a>
    <a href="https://streamlit.io" target="_blank">
      <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
    </a>
    <a href="LICENSE" target="_blank">
      <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License">
    </a>
  </span>
</div>

---

<div style="background-color:#f0f8ff; padding:20px; border-left:6px solid #007ACC; margin-bottom:20px;">
<h2>Project Overview</h2>
<p>The Medical Insurance Cost Predictor estimates annual health insurance costs using demographic and health features. Leveraging feature engineering and Random Forest Regression, it delivers accurate predictions for individuals and healthcare providers.</p>
<ul>
  <li>Estimate insurance costs using age, BMI, number of children, region, gender, and smoker status</li>
  <li>Learn advanced feature engineering and regression techniques</li>
  <li>Deploy ML models interactively with Streamlit for instant predictions</li>
</ul>
</div>

<div style="background-color:#fff8dc; padding:20px; border-left:6px solid #FFA500; margin-bottom:20px;">
<h2>Why This Project Matters</h2>
<p>Healthcare costs are complex and rising, making budgeting and planning challenging for individuals and insurance providers. This project provides:</p>
<ul>
  <li>Quick, data-driven insurance cost estimates to support personal financial planning</li>
  <li>Insights for insurance companies to better understand risk factors</li>
  <li>Interactive web interface for instant predictions without technical expertise</li>
  <li>Hands-on educational insight into machine learning regression, preprocessing, and feature engineering</li>
</ul>
<p>Target Users: Individuals planning healthcare budgets, ML students, healthcare startups, and insurance professionals.</p>
</div>

<div style="background-color:#e6ffe6; padding:20px; border-left:6px solid #32CD32; margin-bottom:20px;">
<h2>Live Web App</h2>
<p>
<a href="https://medical-insurance-cost-predictor.streamlit.app/" target="_blank" style="color:#006400; font-weight:bold;">
Click here to try the Medical Insurance Cost Predictor
</a>
</p>
</div>

<div style="background-color:#fff0f5; padding:20px; border-left:6px solid #C71585; margin-bottom:20px;">
<h2>Dataset Overview — Medical Insurance Dataset</h2>
<p><b>Entries:</b> 1,338 | <b>Columns:</b> 7</p>
<table>
<tr><th>Column</th><th>Description</th></tr>
<tr><td>age</td><td>Age of primary beneficiary</td></tr>
<tr><td>sex</td><td>Gender</td></tr>
<tr><td>bmi</td><td>Body mass index</td></tr>
<tr><td>children</td><td>Number of children covered</td></tr>
<tr><td>smoker</td><td>Smoker status (yes/no)</td></tr>
<tr><td>region</td><td>Residential region (northeast, southeast, southwest, northwest)</td></tr>
<tr><td>charges</td><td>Individual medical costs billed by insurance</td></tr>
</table>
<p><b>Dataset Link:</b> <a href="https://www.kaggle.com/datasets/mirichoi0218/insurance" target="_blank">Kaggle: Medical Insurance Dataset</a></p>
</div>

<div style="background-color:#f5f5dc; padding:20px; border-left:6px solid #8B4513; margin-bottom:20px;">
<h2>Repository Structure</h2>
<pre>
.
📁 Medical_Insurance_Cost_Prediction/
├── profile_img.png                 ← Project banner
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── data/
│   ├── Raw/
│   │   └── insurance.csv       ← Raw Dataset
│   └── Processed/
│       └── cleaned_dataset.csv           ← Cleaned Dataset
|   └── Report/
        └── Medical_Insurance_Cost_Prediction.html ← Summary Report of the Dataset
├── src/
│   ├── file.ipynb                   ← main programming file (preprocessing & training)
├── models/
│   └── model.pkl       ← Random Forest pkl file   
└── app/
    └── app.py                ← Interactive Streamlit web app
</pre>
</div>

<div style="background-color:#e0ffff; padding:20px; border-left:6px solid #20B2AA; margin-bottom:20px;">
<h2>How It Works / Feature Processing</h2>
<ol>
<li><b>Data Cleaning:</b> Remove duplicates, handle missing values, and standardize numeric & categorical data</li>
<li><b>Feature Engineering:</b> Create interaction terms, polynomial features, BMI categories, smoker status encoding, and region one-hot encoding</li>
<li><b>Train-Test Split:</b> Stratified split based on smoker status to maintain proportional distribution</li>
<li><b>Preprocessing Pipeline:</b> OneHotEncoder for nominal features, OrdinalEncoder for ordered categorical features, numeric passthrough</li>
<li><b>Output Transformation:</b> Log transformation of charges for model stability and reducing skew</li>
<li><b>Model Training:</b> Multiple regression models tested (Linear Regression, SVR, Random Forest), with Random Forest achieving highest accuracy</li>
<li><b>Evaluation:</b> Metrics include R², RMSE, and MAE for robust performance assessment</li>
<li><b>Deployment:</b> Streamlit app enables users to input personal information and get real-time predictions</li>
</ol>
</div>

<div style="background-color:#ffe4e1; padding:20px; border-left:6px solid #FF69B4; margin-bottom:20px;">
<h2>Run Locally</h2>
<pre>
git clone https://github.com/harisyar-ai/Medical_Insurance_Cost_Prediction.git
cd Medical_Insurance_Cost_Prediction
pip install -r requirements.txt
streamlit run app/app.py
</pre>
</div>

<div style="background-color:#f0fff0; padding:20px; border-left:6px solid #228B22; margin-bottom:20px;">
<h2>Future Improvements</h2>
<ul>
<li>Add SHAP/LIME visualizations for model explainability</li>
<li>Ensemble stacking for higher prediction accuracy</li>
<li>Include additional demographic, lifestyle, and medical features</li>
<li>Multi-language support for the Streamlit UI</li>
<li>Mobile-friendly responsive version of the web app</li>
</ul>
</div>

<div align="center" style="padding:20px; margin-top:20px; border-top:2px solid #ccc;">
Developed by <b>Haider • Shehzad • Haris</b> — February 2026  
Stars & feedback are highly appreciated  
<br>
<a href="https://github.com/harisyar-ai" target="_blank">github.com/harisyar-ai</a>
</div>
