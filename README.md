### AllLife Bank Personal Loan Prediction Model  

---

#### **Project Overview**  
This project focuses on building a predictive model for AllLife Bank to identify liability customers who are most likely to accept personal loan offers. By targeting these customers effectively, the bank can increase its loan business and earn more interest income.  

#### **Problem Statement**  
AllLife Bank aims to expand its asset customer base by converting liability customers into personal loan customers. With a past campaign showing a 9% conversion rate, this project seeks to enhance customer targeting through predictive modeling, helping the marketing department identify potential borrowers efficiently.  

---

### **Project Workflow**

#### **1. Data Understanding**
The dataset contains customer demographic, financial, and behavioral attributes:
- **Key Variables**: `Age`, `Experience`, `Income`, `Education`, `CCAvg`, `Mortgage`, `Personal_Loan`, etc.  
- **Target Variable**: `Personal_Loan` (0 = No, 1 = Yes).  

---

#### **2. Exploratory Data Analysis (EDA)**  
Key insights from EDA include:  
- **Income**: Higher-income groups are more likely to take loans.  
- **Education**: Advanced degree holders show a higher propensity for loans.  
- **Family Size**: Families with size 3–4 tend to accept more loans.  
- **Credit Card Usage**: Customers with higher average credit card spending are good prospects for loans.  
- **Account Ownership**: Features like `Securities_Account` and `CD_Account` show a moderate influence on loan acceptance.  

---

#### **3. Feature Engineering**  
- **New Features**:  
  - `Income_per_Family`: Ratio of income to family size.  
  - `Mortgage_to_Income`: Mortgage relative to income.  
- **Binning**: Categorized income levels into bins (`Low`, `Medium`, `High`, `Very High`).  
- Outlier treatment: Applied IQR-based filtering to clean the dataset.  

---

#### **4. Model Building**  
- **Model Selection**: Decision Tree Classifier with pruning for better interpretability and performance.  
- **Pruning Outcome**:  
  - Reduced model complexity while maintaining balanced accuracy and recall.  
  - Train-Test Metrics (After Pruning):  
    - Accuracy: 95.4% (Train), 94.8% (Test).  
    - Recall: 100% (Train), 98.6% (Test).  

---

#### **5. Deployment Approach**  
To enable bank staff to make predictions, we are deploying the model via a user-friendly web interface:  
1. **Backend**: Flask to handle the model inference and business logic.  
2. **Frontend**: HTML/CSS for an interactive and visually appealing interface.  
3. **Deployment Platform**: Render or Heroku for hosting.  

---

### **Project Files**
- **Notebook**: Contains EDA, feature engineering, model training, and evaluation.  
- **App Files**: Flask app structure:
  - `app.py`: Backend logic.  
  - `templates/`: HTML files for the frontend.  
  - `static/`: CSS and other assets for styling.  
- **Deployment Configurations**: Render/Heroku deployment scripts.  
