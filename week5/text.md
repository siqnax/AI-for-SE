Part 1: Short Answer Questions 


# 1. Problem Definition 

### 🔍 **Hypothetical AI Problem:**

**"Predicting Hospital Readmission Within 30 Days"**

---

### 🎯 **Objectives:**

1. **Predict** whether a patient is likely to be readmitted within 30 days of discharge.
2. **Identify risk factors** (e.g., comorbidities, age, prior admissions) contributing to readmission.
3. **Enable hospitals** to take preventative action and reduce avoidable readmissions.

---

### 👥 **Stakeholders:**

1. **Hospital Administrators** – Aim to improve patient outcomes and reduce costs.
2. **Healthcare Providers (Doctors/Nurses)** – Use predictions to tailor post-discharge care plans.

---

### 📏 **Key Performance Indicator (KPI):**

**Readmission Prediction Accuracy (AUC-ROC Score ≥ 0.85)**
Measures how well the AI model distinguishes between patients who will and won't be readmitted.






# 2. Data Collection & Preprocessing 

**"Predicting student dropout rates in universities."**

---

### **1. Identify 2 Data Sources**

* **University Student Information System (SIS):** Contains demographic data, academic records, attendance logs, and financial aid status.
* **Learning Management System (LMS):** Tracks student engagement such as login frequency, assignment submissions, and time spent on course materials.

---

### **2. Explain 1 Potential Bias in the Data**

* **Digital Engagement Bias:** Students with limited internet access or poor digital literacy may appear less engaged in LMS data, even though they are actively learning through offline resources. This can bias the model into incorrectly labeling such students as high dropout risks.

---

### **3. Outline 3 Preprocessing Steps**

1. **Handle Missing Data:**

   * Use imputation methods (e.g., mean for numerical, mode for categorical) or remove records with excessive missing values.

2. **Normalize Numerical Features:**

   * Apply min-max scaling or z-score normalization to ensure features like GPA and attendance rates are on comparable scales.

3. **Encode Categorical Variables:**

   * Use one-hot encoding or label encoding for features like gender, major, or course type.











# 3. Model Development 

### **Model Choice: `Random Forest`**

**Justification:**

* **Handles Mixed Data Types:** Can work well with both numerical and categorical features without heavy preprocessing.
* **Robust to Overfitting:** Ensemble method that reduces variance by averaging many decision trees.
* **Feature Importance:** Easily interpretable, helping educators understand which factors most influence dropout risk.


### **Data Splitting Strategy:**

* **Training Set (70%)** – Used to train the Random Forest model.
* **Validation Set (15%)** – Used for tuning hyperparameters and selecting the best model configuration.
* **Test Set (15%)** – Used to evaluate final model performance on unseen data.

*Stratified sampling* would be used to ensure that each set maintains the same proportion of dropout vs. non-dropout cases, especially if the data is imbalanced.

---

### **2 Hyperparameters to Tune:**

1. **`n_estimators` (number of trees):**

   * Affects model accuracy and computation time. More trees usually improve performance but increase training time.

2. **`max_depth` (maximum depth of trees):**

   * Controls how complex each tree can be. Helps prevent overfitting by limiting tree depth.










