import streamlit as st
import pandas as pd
import numpy as np
import pickle
import traceback

st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Styling ────────────────────────────────────────────────────────────────
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #e0e0e0;
    }

    .main-title {
        font-size: 3.4rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #00d4ff, #7cffc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 1rem 0 0.6rem;
        text-shadow: 0 4px 15px rgba(0, 212, 255, 0.45);
    }

    .subtitle {
        text-align: center;
        color: #a0d0ff;
        font-size: 1.3rem;
        margin-bottom: 2.2rem;
    }

    .card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.9rem;
        border: 1px solid rgba(255,255,255,0.12);
        margin-bottom: 1.6rem;
        transition: all 0.32s ease;
        box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    }

    .card:hover {
        transform: translateY(-9px);
        box-shadow: 0 18px 50px rgba(0, 212, 255, 0.28);
        border-color: rgba(0, 212, 255, 0.42);
    }

    .result-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 2.6rem 1.8rem;
        text-align: center;
        color: white;
        margin: 2.5rem 0;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.45);
        border: 1px solid rgba(255,255,255,0.18);
    }

    .result-amount {
        font-size: 3.8rem;
        font-weight: 900;
        margin: 0.7rem 0;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a2a44 0%, #0f1e33 100%) !important;
        border-right: 1px solid rgba(0, 212, 255, 0.15);
    }

    .sidebar-title {
        color: #00d4ff;
        font-size: 1.65rem;
        font-weight: 700;
        margin: 1.6rem 0 1.8rem;
        text-align: center;
    }

    /* Button styling - UPDATED TO MATCH OTHER INPUTS */
    .stButton > button {
        background: linear-gradient(135deg, #1a2a44 0%, #0f1e33 100%);
        color: #00d4ff;
        font-weight: 700;
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 12px;
        padding: 0.9rem 2.2rem;
        transition: all 0.28s ease;
    }

    .stButton > button:hover {
        transform: translateY(-6px);
        box-shadow: 0 14px 36px rgba(0, 212, 255, 0.25);
        border-color: rgba(0, 212, 255, 0.6);
    }

    /* Selectbox styling */
    .stSelectbox > div > div {
        background: linear-gradient(135deg, #1a2a44 0%, #0f1e33 100%);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 8px;
        transition: all 0.28s ease;
    }

    .stSelectbox > div > div:hover {
        transform: translateY(-6px);
        border-color: rgba(0, 212, 255, 0.6);
        box-shadow: 0 14px 36px rgba(0, 212, 255, 0.25);
    }

    /* Radio button styling */
    .stRadio > div {
        background: linear-gradient(135deg, #1a2a44 0%, #0f1e33 100%);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 8px;
        padding: 0.8rem;
        transition: all 0.28s ease;
    }

    .stRadio > div:hover {
        transform: translateY(-6px);
        border-color: rgba(0, 212, 255, 0.6);
        box-shadow: 0 14px 36px rgba(0, 212, 255, 0.25);
    }

    /* Slider styling */
    .stSlider {
        transition: all 0.28s ease;
    }

    .stSlider:hover {
        transform: translateY(-6px);
    }

    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #00d4ff, #7cffc4) !important;
    }

    /* Number input styling - COMPLETELY REDESIGNED TO MATCH OTHER INPUTS */
    /* Hide the increment/decrement buttons */
    .stNumberInput button {
        display: none !important;
    }

    /* Style the wrapper div to match selectbox/radio behavior */
    .stNumberInput [data-baseweb="input"] {
        background: linear-gradient(135deg, #1a2a44 0%, #0f1e33 100%) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 8px !important;
        transition: all 0.28s ease !important;
    }

    .stNumberInput:hover [data-baseweb="input"] {
        transform: translateY(-6px) !important;
        border-color: rgba(0, 212, 255, 0.6) !important;
        box-shadow: 0 14px 36px rgba(0, 212, 255, 0.25) !important;
    }

    /* Style the actual input inside */
    .stNumberInput input {
        background: transparent !important;
        color: #00d4ff !important;
        font-weight: 600 !important;
        border: none !important;
    }

    .stNumberInput input:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    /* Alternative approach - target the root div */
    .stNumberInput > div {
        transition: all 0.28s ease !important;
    }

    .stNumberInput > div > div {
        background: linear-gradient(135deg, #1a2a44 0%, #0f1e33 100%) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 8px !important;
        transition: all 0.28s ease !important;
    }

    .stNumberInput:hover > div > div {
        transform: translateY(-6px) !important;
        border-color: rgba(0, 212, 255, 0.6) !important;
        box-shadow: 0 14px 36px rgba(0, 212, 255, 0.25) !important;
    }

    hr {
        border-color: rgba(0, 212, 255, 0.22);
        margin: 2.8rem 0;
    }

    /* Team member card with hover effect */
    .team-card {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(8px);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid rgba(255,255,255,0.12);
        margin-bottom: 1rem;
        text-align: center;
        transition: all 0.28s ease;
        box-shadow: 0 6px 20px rgba(0,0,0,0.30);
    }

    .team-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 14px 36px rgba(0, 212, 255, 0.25);
        border-color: rgba(0, 212, 255, 0.45);
    }

    .team-card h2 {
        color: #00d4ff;
        font-size: 1.5rem;
        margin: 0 0 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# ─── Model loading with better diagnostics ──────────────────────────────────
@st.cache_resource
def load_model():
    path = "models/model.pkl"  # Use forward slashes, no 'r' prefix needed
    try:
        with open(path, 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error(f"Model file not found: {path}")
        return None
    except Exception as e:
        st.error(f"Model loading failed: {str(e)}")
        with st.expander("Full traceback"):
            st.code(traceback.format_exc())
        return None
model = load_model()

# Early exit if model cannot be loaded
if model is None:
    st.warning("The prediction model could not be loaded. Prediction features are disabled.")
    st.info("Please verify that the file exists and is a valid pickled model:\n" + 
            # r"F:\PYTHON\ML_Projects\Medical_Insurance_Cost_Prediction\models\model.pkl")
            r"Medical_Insurance_Cost_Prediction\models\model.pkl")

# ─── Feature engineering ────────────────────────────────────────────────────
def add_engineered_features(df):
    df = df.copy()
    df['smoker_binary'] = df['smoker'].map({'no': 0, 'yes': 1}).astype(int)

    df['smoker_age']      = df['smoker_binary'] * df['age']
    df['smoker_bmi']      = df['smoker_binary'] * df['bmi']
    df['smoker_age_bmi']  = df['smoker_binary'] * df['age'] * df['bmi']
    df['smoker_children'] = df['smoker_binary'] * df['children']

    df['age_bmi']       = df['age'] * df['bmi']
    df['age_children']  = df['age'] * df['children']
    df['bmi_children']  = df['bmi'] * df['children']

    df['age_squared']   = df['age'] ** 2
    df['bmi_squared']   = df['bmi'] ** 2

    df['has_children']  = (df['children'] > 0).astype(int)

    df['bmi_category'] = pd.cut(
        df['bmi'],
        bins=[0, 18.5, 25, 30, 35, 100],
        labels=['underweight', 'normal', 'overweight', 'obese_1', 'obese_2'],
        include_lowest=True
    ).astype(str)

    df['age_group'] = pd.cut(
        df['age'],
        bins=[0, 25, 35, 45, 55, 100],
        labels=['18-25', '26-35', '36-45', '46-55', '55+'],
        include_lowest=True
    ).astype(str)

    return df

# ─── Prediction logic ───────────────────────────────────────────────────────
def predict_cost(input_dict):
    if model is None:
        return None

    try:
        df = pd.DataFrame([input_dict])
        df = add_engineered_features(df)
        log_pred = model.predict(df)[0]
        return float(np.expm1(log_pred))
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
        with st.expander("Details"):
            st.code(traceback.format_exc())
        return None

# ─── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">Medical Insurance Smart AI Predictor</div>', unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["Make Prediction", "Recent Predictions", "Project Info", "About Us"],
        label_visibility="collapsed"
    )

# Session state
if "recent_predictions" not in st.session_state:
    st.session_state.recent_predictions = []

# ─── Pages ──────────────────────────────────────────────────────────────────
if page == "Make Prediction":
    st.markdown('<h1 class="main-title">🩺 Medical Insurance Cost Predictor </h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Accurate AI-powered estimation of annual medical insurance costs</p>', unsafe_allow_html=True)

    if model is None:
        st.warning("Prediction is currently unavailable — model could not be loaded.")
    else:
        with st.form("patient_form"):
            col1, col2 = st.columns(2)

            with col1:
                age = st.number_input("Age", min_value=18, max_value=100, value=35, step=1)
                bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
                children = st.number_input("Number of Children", min_value=0, max_value=5, value=0, step=1)

            with col2:
                sex = st.selectbox("Gender", ["male", "female"])
                smoker = st.radio("Smoker?", ["no", "yes"], horizontal=True)
                region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

            submitted = st.form_submit_button("Calculate Estimated Cost", use_container_width=True)

        if submitted:
            input_data = {
                "age": age,
                "sex": sex,
                "bmi": bmi,
                "children": children,
                "smoker": smoker,
                "region": region
            }

            with st.spinner("Calculating..."):
                cost = predict_cost(input_data)

            if cost is not None:
                st.markdown(f"""
                    <div class="result-box">
                        <div style="font-size:1.45rem; opacity:0.92;">Estimated Annual Cost</div>
                        <div class="result-amount">${cost:,.0f}</div>
                        <div style="font-size:1.1rem; margin-top:0.9rem; opacity:0.84;">
                            (model estimate — actual costs may vary)
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                st.session_state.recent_predictions.append({
                    "Age": age,
                    "BMI": round(bmi, 1),
                    "Children": children,
                    "Gender": sex.title(),
                    "Smoker": smoker.upper(),
                    "Region": region.title(),
                    "Estimated Cost": f"${cost:,.0f}"
                })

elif page == "Recent Predictions":
    st.markdown('<h1 class="main-title">🩺 Medical Insurance Cost Predictor </h1>', unsafe_allow_html=True)

    if st.session_state.recent_predictions:
        df = pd.DataFrame(st.session_state.recent_predictions)
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No predictions have been made yet.")

elif page == "Project Info":
    st.markdown('<h1 class="main-title">🩺 Medical Insurance Cost Predictor </h1>', unsafe_allow_html=True)

    st.markdown("""
**Medical Insurance Cost Predictor** is a machine learning application that estimates 
annual health insurance charges based on demographic and health-related features.

**Main characteristics:**
- Trained on real medical insurance data
- Uses extensive feature engineering (interactions, polynomials, binning)
- Random Forest model trained on log-transformed charges
- Typical test R² score: 0.88 – 0.90+
- Modern interface built with Streamlit

**Important:** This is only an estimate. Real insurance prices depend on many factors not included in this model.
    """)

elif page == "About Us":
    st.markdown('<h1 class="main-title">🩺 Medical Insurance Cost Predictor </h1>', unsafe_allow_html=True)

    cols = st.columns(3)

    with cols[0]:
        st.markdown('''
        <div class="team-card">
            <h2>Haider Haroon</h2>
            <p style="text-align: left; margin: 0;">
                • AI Engineer<br>
                • Specializing in AI Security & Computer Vision<br>
                • Passionate about building secure, real-world AI systems<br>
                • Experienced in deploying AI solutions across various industries
            </p>
        </div>
        ''', unsafe_allow_html=True)

    with cols[1]:
        st.markdown('''
        <div class="team-card">
            <h2>Shehzad Haider</h2>
            <p style="text-align: left; margin: 0;">
                • AI Strategy & Innovation Expert<br>
                • Focused on turning research into business value and scalable products<br>
                • Experienced in AI Business Analysis and Product Management<br>
                • Driven to bridge the gap between AI technology and market needs
            </p>
        </div>
        ''', unsafe_allow_html=True)

    with cols[2]:
        st.markdown('''
        <div class="team-card">
            <h2>Haris Yar</h2>
            <p style="text-align: left; margin: 0;">
                • Self-taught AI Developer<br>
                • Enthusiast in Machine Learning and Computer Vision<br>
                • Committed to continuous learning and innovation in AI Research<br>
                • Aspiring to contribute to impactful AI solutions
            </p>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### Connect")
    st.markdown("""
**Muhammad Haris**  
GitHub: https://github.com/harisyar-ai  
LinkedIn: https://www.linkedin.com/in/muhammad-haris-afridi  
Email: mharisyar.ai@gmail.com
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align:center; color:#a0d0ff; padding:2rem 0; font-size:0.95rem;">
        © Built by Haider • Shehzad • Haris  | 2026
    </div>
""", unsafe_allow_html=True)
