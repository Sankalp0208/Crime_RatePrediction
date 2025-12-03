import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model + Dataset
# -----------------------------
model = joblib.load("crime_risk_model.pkl")
df = pd.read_csv("01_District_wise_crimes_committed_IPC_2001_2012.csv")

st.title("🔥 Crime Risk Prediction App")
st.write("Select details to predict district crime risk level (0 = Low, 1 = Medium, 2 = High Risk).")

# -----------------------------
# Dropdowns for State, District, Year
# -----------------------------
states = sorted(df["STATE/UT"].unique())
state = st.selectbox("Select State", states)

districts = sorted(df[df["STATE/UT"] == state]["DISTRICT"].unique())
district = st.selectbox("Select District", districts)

years = sorted(df[df["DISTRICT"] == district]["YEAR"].unique())
year = st.selectbox("Select Year", years)

# -----------------------------
# Crime category selection
# -----------------------------
crime_columns = [
    'MURDER', 'ATTEMPT TO MURDER',
    'CULPABLE HOMICIDE NOT AMOUNTING TO MURDER', 'RAPE',
    'CUSTODIAL RAPE', 'OTHER RAPE', 'KIDNAPPING & ABDUCTION',
    'KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS',
    'KIDNAPPING AND ABDUCTION OF OTHERS', 'DACOITY',
    'PREPARATION AND ASSEMBLY FOR DACOITY', 'ROBBERY', 'BURGLARY',
    'THEFT', 'AUTO THEFT', 'OTHER THEFT', 'RIOTS',
    'CRIMINAL BREACH OF TRUST', 'CHEATING', 'COUNTERFIETING',
    'ARSON', 'HURT/GREVIOUS HURT', 'DOWRY DEATHS',
    'ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY',
    'INSULT TO MODESTY OF WOMEN',
    'CRUELTY BY HUSBAND OR HIS RELATIVES',
    'IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES',
    'CAUSING DEATH BY NEGLIGENCE'
]

crime_type = st.selectbox("Select Crime Category", crime_columns)
crime_value = st.number_input(f"Enter Count for {crime_type}", min_value=0, step=1)

# ------------------------------------------------------
# EXACT TRAINING FEATURES (30 features including 'index')
# ------------------------------------------------------
feature_columns = [
    'index', 'YEAR', 'MURDER', 'ATTEMPT TO MURDER',
    'CULPABLE HOMICIDE NOT AMOUNTING TO MURDER', 'RAPE',
    'CUSTODIAL RAPE', 'OTHER RAPE', 'KIDNAPPING & ABDUCTION',
    'KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS',
    'KIDNAPPING AND ABDUCTION OF OTHERS', 'DACOITY',
    'PREPARATION AND ASSEMBLY FOR DACOITY', 'ROBBERY', 'BURGLARY',
    'THEFT', 'AUTO THEFT', 'OTHER THEFT', 'RIOTS',
    'CRIMINAL BREACH OF TRUST', 'CHEATING', 'COUNTERFIETING',
    'ARSON', 'HURT/GREVIOUS HURT', 'DOWRY DEATHS',
    'ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY',
    'INSULT TO MODESTY OF WOMEN',
    'CRUELTY BY HUSBAND OR HIS RELATIVES',
    'IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES',
    'CAUSING DEATH BY NEGLIGENCE'
]

# ------------------------------------------------------
# Prepare Input EXACTLY in model format
# ------------------------------------------------------
input_dict = {col: 0 for col in feature_columns}

input_dict["index"] = 0                 # model expects index column
input_dict["YEAR"] = year               # fill year
input_dict[crime_type] = crime_value    # fill selected crime value

input_df = pd.DataFrame([input_dict])


# ------------------------------------------------------
# Predict Button
# ------------------------------------------------------
if st.button("Predict Risk Level"):
    prediction = model.predict(input_df)[0]

    st.subheader("📌 Prediction Result:")
    if prediction == 0:
        st.success("🟢 LOW RISK DISTRICT")
    elif prediction == 1:
        st.warning("🟡 MEDIUM RISK DISTRICT")
    else:
        st.error("🔴 HIGH RISK DISTRICT")
