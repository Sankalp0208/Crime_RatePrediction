# 🔥 Crime Risk Prediction System (India IPC Crime Data)

This project predicts **crime risk levels** for districts in India using **machine learning ensemble models** trained on the *District-wise Crimes Committed–IPC 2001–2012* dataset. <br>

The system classifies each district-year into:<br>

- **0 → Low Risk** <br>
- **1 → Medium Risk** <br>
- **2 → High Risk** <br>

A fully interactive **Streamlit web application** allows users to select a **State, District, Year, and Crime Category** to predict the Crime Risk Level. <br>

--- <br>

## 📌 Project Overview<br>

### ✔ Machine Learning Techniques Used<br>
This project uses **ensemble learning** combining multiple base learners:<br>

- **Decision Tree** <br>
- **Support Vector Machine (SVM)** <br>
- **Random Forest** <br>
- **Logistic Regression** <br>

To improve prediction performance, a **Stacking Classifier** is used with: <br>

- **Base Learners:** DT, SVM, RF, LR   <br>
- **Meta Learner:** Logistic Regression   <br>

--- <br>

## 📂 Dataset Used <br>

The dataset used: 01_District_wise_crimes_committed_IPC_2001_2012 <br>

