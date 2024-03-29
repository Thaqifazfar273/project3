# -*- coding: utf-8 -*-
"""project3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dvq04WzRErkkd9sVq8zKvxjuzjqbeO4r

**PROJECT 3 (10 MARKS) !!!**

Use the following Telco dataset :
    https://www.kaggle.com/datasets/blastchar/telco-customer-churn
and perform the following tasks:

(1) EDA

(2) What determines the reasons for customers to give up the services
"""

#from google.colab import drive
#drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

df=pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
df.head()

df.tail()

df

df.shape

df.info()

df.dtypes

df.describe()

df.max()

df.min()

df.std()

df.mean()

df.median()

!pip install sweetviz

# importing sweetviz library
import sweetviz as sv

#analyzing the dataset
advert_report = sv.analyze(df)

#display the report
advert_report.show_html('Advertising.html')

advert_report.show_notebook()

plt.figure(figsize=(5, 4))
sns.heatmap(df.corr(), annot=True, fmt=".2F", linewidth=.5)
plt.show()

"""**QUESTION 2**

Descriptive Analysis Question:
Question: What is the distribution of customer churn across different contract types?
"""

import pandas as pd

# Load the dataset
telco_data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Calculate churn distribution by contract type
contract_churn_distribution = telco_data.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()

print(contract_churn_distribution)

"""Exploratory Analysis Question:
Question: How do monthly charges vary between churned and non-churned customers?
"""

import matplotlib.pyplot as plt

# Plot distribution of monthly charges for churned and non-churned customers
plt.figure(figsize=(10, 6))
sns.boxplot(x='Churn', y='MonthlyCharges', data=telco_data)
plt.title('Monthly Charges Distribution by Churn')
plt.show()

"""Inferential Analysis Question:
Question: Is there a significant difference in tenure between churned and non-churned customers?
"""

from scipy.stats import ttest_ind

# Perform t-test to compare tenure between churned and non-churned customers
churned_tenure = telco_data[telco_data['Churn'] == 'Yes']['tenure']
non_churned_tenure = telco_data[telco_data['Churn'] == 'No']['tenure']

t_stat, p_value = ttest_ind(churned_tenure, non_churned_tenure)
print("T-statistic:", t_stat)
print("P-value:", p_value)

"""Predictive Analysis Question:
Question: Can we predict customer churn based on their contract type, monthly charges, and tenure?
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Prepare features and target variable
X = telco_data[['Contract', 'MonthlyCharges', 'tenure']]
y = telco_data['Churn']

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Predict churn on the test set
y_pred = rf_classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""Causal Analysis Question:
Question: Does the presence of additional services (e.g., streaming TV, online security) cause customers to churn?
"""

# Calculate churn rate for customers with and without additional services
additional_services_churn_rate = telco_data.groupby('MultipleLines')['Churn'].value_counts(normalize=True).unstack()

print(additional_services_churn_rate)

"""Mechanistic Analysis Question:
Question: How does the availability of tech support influence customer churn rates?
"""

# Plot churn rate by tech support availability
plt.figure(figsize=(10, 6))
sns.barplot(x='TechSupport', y='Churn', data=telco_data, ci=None)
plt.title('Churn Rate by Tech Support Availability')
plt.xlabel('Tech Support Availability')
plt.ylabel('Churn Rate')
plt.show()

"""###Answer to the Question

Contract flexibility: Month-to-month agreements had higher rates of contract turnover, indicating that contract flexibility may be a factor in churn.

Pricing impact: Variations in monthly fees between non-churned and churned clients show how pricing tactics affect customer retention.

Relationship duration: Tenure is important because longer-lasting connections have lower churn rates.

Predictive power: Elements such as tenure, charges, and contract type can predict attrition and help understand consumer behaviour.

Service influence: Churn rates are impacted by the availability of services such as tech support, highlighting the importance of service offerings in retention.

"""