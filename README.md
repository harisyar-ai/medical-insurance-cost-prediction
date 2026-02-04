# 🩺 Medical Insurance Cost Prediction 2026
### AI-Powered Prediction Using Random Forest & Feature Engineering

<div align="center" style="margin-bottom:20px;">
  <img src="insurance_banner.jpeg" alt="Medical Insurance Cost Predictor" width="95%">
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
<h2> Project Overview</h2>
<p>The <b>Medical Insurance Cost Predictor</b> estimates annual health insurance costs using demographic and health features. Leveraging <b>feature engineering</b> and <b>Random Forest Regression</b>, it delivers accurate predictions.</p>
<ul>
  <li>Estimate insurance costs using age, BMI, children, region, gender, and smoker status</li>
  <li>Learn advanced feature engineering and regression techniques</li>
  <li>Deploy ML models interactively with <b>Streamlit</b></li>
</ul>
</div>

<div style="background-color:#fff8dc; padding:20px; border-left:6px solid #FFA500; margin-bottom:20px;">
<h2> Why This Project Matters</h2>
<p>Predicting healthcare costs is complex. This project provides:</p>
<ul>
  <li>Quick, data-driven insurance cost estimates</li>
  <li>Interactive web interface for instant predictions</li>
  <li>Educational insight into ML regression and preprocessing</li>
</ul>
<p><b>Target Users:</b> Individuals planning healthcare budgets, ML students, healthcare startups</p>
</div>

<div style="background-color:#e6ffe6; padding:20px; border-left:6px solid #32CD32; margin-bottom:20px;">
<h2> Live Web App</h2>
<p>
<a href="https://medical-insurance-cost-predictor.streamlit.app/" target="_blank" style="color:#006400; font-weight:bold;">
Click here to try the Medical Insurance Cost Predictor
</a>
</p>
</div>

<div style="background-color:#fff0f5; padding:20px; border-left:6px solid #C71585; margin-bottom:20px;">
<h2> Dataset Overview — Medical Insurance Dataset</h2>
<p><b>Entries:</b> 1,338 | <b>Columns:</b> 7</p>
<table>
<tr><th>Column</th><th>Description</th></tr>
<tr><td>age</td><td>Age of primary beneficiary</td></tr>
<tr><td>sex</td><td>Gender</td></tr>
<tr><td>bmi</td><td>Body mass index</td></tr>
<tr><td>children</td><td>Number of children covered</td></tr>
<tr><td>smoker</td><td>Smoker status (yes/no)</td></tr>
<tr><td>region</td><td>Residential region (northeast, southeast...)</td></tr>
<tr><td>charges</td><td>Individual medical costs billed by insurance</td></tr>
</table>
<p><b>Dataset Link:</b> <a href="https://www.kaggle.com/datasets/mirichoi0218/insurance" target="_blank">Kaggle: Medical Insurance Dataset</a></p>
</div>
---
<div style="background-color:#f5f5dc; padding:20px; border-left:6px solid #8B4513; margin-bottom:20px;">
<h2> Repository Structure</h2>
<pre>.
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
---  
</div>

<div style="background-color:#e0ffff; padding:20px; border-left:6px solid #20B2AA; margin-bottom:20px;">
<h2> How It Works</h2>
<ol>
<li><b>Data Cleaning & Preprocessing:</b> Remove duplicates & missing values, standardize numeric & categorical features</li>
<li><b>Feature Engineering:</b> Interactions, polynomial features, binning, derived features</li>
<li><b>Train-Test Split:</b> Stratified split by smoker status</li>
<li><b>Preprocessing Pipeline:</b> OneHotEncoder, OrdinalEncoder, numeric passthrough</li>
<li><b>Output Transformation:</b> Log transformation of charges for stability</li>
<li><b>Model Training & Evaluation:</b> Tested multiple models; Random Forest performed best</li>
<li><b>Deployment:</b> Streamlit UI with dynamic predictions</li>
</ol>
</div>

<div style="background-color:#ffe4e1; padding:20px; border-left:6px solid #FF69B4; margin-bottom:20px;">
<h2> Run Locally</h2>
<pre>
git clone https://github.com/harisyar-ai/Medical_Insurance_Cost_Prediction.git
cd Medical_Insurance_Cost_Prediction
pip install -r requirements.txt
streamlit run app/app.py
</pre>
</div>

<div style="background-color:#f0fff0; padding:20px; border-left:6px solid #228B22; margin-bottom:20px;">
<h2> Future Improvements</h2>
<ul>
<li>Add SHAP/LIME visualizations for explainability</li>
<li>Ensemble stacking for better predictions</li>
<li>Include more demographic & lifestyle features</li>
<li>Multi-language Streamlit UI</li>
<li>Mobile-friendly responsive version</li>
</ul>
</div>
---
                            December 2025
                 Developed by Haider • Shehzad • Haris
              Stars & feedback are highly appreciated ⭐
  
                      github.com/harisyar-ai
