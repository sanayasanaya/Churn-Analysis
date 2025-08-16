#!/usr/bin/env python
# coding: utf-8

# In[109]:


pip install pandas


# In[110]:


pip install --upgrade seaborn pandas


# In[111]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[112]:


df = pd.read_csv ('Customer Churn.csv')


# In[113]:


df.head()


# In[ ]:





# In[114]:


df.info()


# #replace the black into 0 (because tenure is 0) and covert the data type into float

# In[115]:


df["TotalCharges"] = df["TotalCharges"].replace(" ","0")
df["TotalCharges"] = df["TotalCharges"].astype("float")


# In[ ]:





# In[116]:


df.info()


# In[117]:


df.isnull()


# In[118]:


df.isnull().sum()


# In[119]:


#overall sum
df.isnull().sum().sum()


# In[120]:


df.describe()


# #check duplicate data

# In[121]:


df.duplicated()


# In[122]:


df.duplicated().sum()


# In[123]:


df["customerID"].duplicated().sum()


# In[124]:


# conver 0/1 value of senior citizen into yes/no for easy to understand.


# In[125]:


def convert(value):
    if value == 2:
        return "yes"
    else:
        return "no"
    
df['SeniorCitizen'] = df['SeniorCitizen'].apply(convert)


# In[126]:


df.head()


# In[127]:


# why customer churn


# In[128]:


plt.figure(figsize = (3,3.3))
ax = sns.countplot(x = 'Churn', data = df)

ax.bar_label(ax.containers[0])
plt.title("Count of Customer by Churn")
plt.show()


# In[129]:


gb = df.groupby("Churn").agg({'Churn':'count'})
gb


# In[130]:


plt.figure(figsize = (3,3))
plt.title("Percentage of Churn Customer" , fontsize = 10)
plt.pie(gb['Churn'], labels = gb.index, autopct = "%1.2f%%")
plt.show()


# 26.54% of customer are Churned out.
# Now explore the reason behind it.

# In[131]:


plt.figure(figsize = (4,4))
plt.title("Churn by Gender")
sns.countplot(x="gender", data = df , hue = "Churn")
plt.show()


# In[132]:


plt.figure(figsize = (3,3))
plt.title("Churn by Senior Citizen")
sns.countplot( x ="SeniorCitizen", data = df , hue = "Churn")
plt.show()


# In[133]:


plt.figure(figsize = (2,2))
ax = sns.countplot(x = "SeniorCitizen", data = df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Senior Citizen")
plt.show()


# In[134]:


total_counts = df.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack() * 100

# Plot
fig, ax = plt.subplots(figsize=(4, 4))  # Adjust figsize for better visualization

# Plot the bars
total_counts.plot(kind='bar', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e'])  # Customize colors if desired

# Add percentage labels on the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.text(x + width / 2, y + height / 2, f'{height:.1f}%', ha='center', va='center')

plt.title('Churn by Senior Citizen (Stacked Bar Chart)')
plt.xlabel('SeniorCitizen')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn', bbox_to_anchor = (0.9,0.9))  # Customize legend location

plt.show()


# In[135]:


#people who have used our services for a long time have stayed and people who have used our sevices 1 or 2 months have churned

#comparative a greater pecentage of people in senior citizen category have churned

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

plt.figure(figsize = (9,4))
sns.histplot(x = "tenure", data = df, bins = 72, hue = "Churn")
plt.show()


# In[136]:


plt.figure(figsize = (4,4))
ax = sns.countplot(x = "Contract", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Contract")
plt.show()


# In[137]:


df.columns.values


# # The majority of customers who do not churn tend to have services like PhoneService, InternetService (particularly DSL), and OnlineSecurity enabled. For services like OnlineBackup, TechSupport, and StreamingTV, churn rates are noticeably higher when these services are not used or are unavailable.

# In[138]:


columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

# Number of columns for the subplot grid (you can change this)
n_cols = 3
n_rows = (len(columns) + n_cols - 1) // n_cols  # Calculate number of rows needed

# Create subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))  # Adjust figsize as needed

# Flatten the axes array for easy iteration (handles both 1D and 2D arrays)
axes = axes.flatten()

# Iterate over columns and plot count plots
for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, ax=axes[i], hue = df["Churn"])
    axes[i].set_title(f'Count Plot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')

# Remove empty subplots (if any)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


# In[ ]:





# In[139]:


#customer is likely to churn when he is using electronic check as a payment method


plt.figure(figsize = (6,4))
ax = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned Customers by Payment Method")
plt.xticks(rotation = 45)
plt.show()

