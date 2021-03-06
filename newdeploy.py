#!/usr/bin/env python
# coding: utf-8

# In[191]:


import pandas as pd 
import streamlit as st
from pickle import load
import seaborn as sns
from pickle import dump
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import base64


# In[192]:


loaded_model=load(open('svm_model.sav','rb'))


# In[193]:


df=pd.read_csv("Ecommerce.csv")
df=df.drop("Customer ID",axis=1)
df=df.rename({'Avg Session length':'Avg_Session_length','Time on App':'Time_on_App','Time on Website':'Time_on_Website','Length of MemberShip':'Length_of_MemberShip','Yealy amount spent':'Yealy_amount_spent'},axis=1)


# In[194]:


st.title('Model Deployment: Support Vector Regresor')
    


# In[195]:


view_data = st.checkbox('View Data')
view_columns=st.checkbox('View features')
if view_data:
    st.write(df)
if view_columns:
    st.write(df.columns)


# In[196]:


view=st.checkbox("Pairplot")
if view:  
     st.pyplot(sns.pairplot(df))


# In[197]:


def welcome():
    return 'welcome all'


# In[198]:


def prediction(Avg_Session_length,Time_on_App,Time_on_Website,Length_of_MemberShip):  
   
    prediction = loaded_model.predict(
        [[Avg_Session_length,Time_on_App,Time_on_Website,Length_of_MemberShip]])
    print(prediction)
    return prediction


# In[199]:


def main():
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Ecommerce Annual Income Prediction App </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    
    
    Avg_Session_length= st.text_input("Avg Session length", "")
    Time_on_App= st.text_input("Time on App", "")
    Time_on_Website= st.text_input("Time on Website", "")
    Length_of_MemberShip= st.text_input("Length of MemberShip", "")
    result =""
    
    if st.button("Predict"):
        result = prediction(Avg_Session_length,Time_on_App,Time_on_Website,Length_of_MemberShip)
    st.success('The output is {}'.format(result))
if __name__=='__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:




