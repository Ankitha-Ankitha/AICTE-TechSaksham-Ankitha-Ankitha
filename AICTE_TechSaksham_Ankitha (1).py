#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[11]:


shop = pd.read_csv('Downloads/shopping_trends_updated.csv')


# In[13]:


shop.head()


# In[15]:


shop.shape


# In[17]:


shop.dtypes


# In[19]:


shop.columns


# In[21]:


shop.info()


# In[23]:


shop.isnull().sum()


# In[33]:


print(f"The unique values of the 'Gender' column are: {shop['Gender'].unique()}")
print()
print(f"The unique values of the 'Category' column are: {shop['Category'].unique()}")
print()
print(f"The unique values of the 'Size' column are: {shop['Size'].unique()}")
print()
print(f"The unique values of the 'Subscription Status' column are: {shop['Subscription Status'].unique()}")
print()
print(f"The unique values of the 'Shipping Type' column are: {shop['Shipping Type'].unique()}")
print()
print(f"The unique values of the 'Discount Applied' column are: {shop['Discount Applied'].unique()}")
print()
print(f"The unique values of the 'Promo Code Used' column are: {shop['Promo Code Used'].unique()}")
print()
print(f"The unique values of the 'Payment Method' column are: {shop['Payment Method'].unique()}")
print()

1.What is the overall distribution of customer ages in the dataset?
# In[74]:


shop['Age'].value_counts()


# In[37]:


shop['Age'].mean()


# In[41]:


shop['Gender'].unique()


# In[47]:


shop['Age_category']=pd.cut(shop['Age'], bins=[0,15,18,30,50,70], labels=['child','teen','Young Adults','Middle-Aged Adults','old'])


# In[49]:


fig=px.histogram(shop, y='Age', x='Age_category')
fig.show()


# 2.How does the average purchase amount vary across different product categories?

# In[61]:


shop.columns


# In[57]:


shop['Category'].unique()


# In[59]:


shop.groupby('Category')['Purchase Amount (USD)'].mean()


# In[78]:


shop[['Category','Purchase Amount (USD)']]


# 3.Which gender has the highest number of purchases?

# In[63]:


shop.columns


# In[65]:


sns.barplot(shop, x='Gender', y='Purchase Amount (USD)')

4.What are the most commonly purchased items in each category?
# In[67]:


shop.columns


# In[69]:


shop.groupby('Category')['Item Purchased'].value_counts()


# In[71]:


fig=px.histogram(shop,x='Item Purchased',color='Category')
fig.show()

5.Are there any specific seasons or months where customer spending is significantly higher?
# In[80]:


shop['Season'].unique()


# In[82]:


shop['Season'].value_counts()


# In[84]:


fig=px.histogram(shop,x='Season',range_y=[800,1200])
fig.show()

6.What is the average rating given by customers for each product category?
# In[96]:


shop.groupby('Category')['Review Rating'].mean()


# In[92]:


shop_groupby=shop.groupby('Category')['Review Rating'].mean().reset_index()
print(shop_groupby)


# In[94]:


fig=px.bar(shop_groupby,x='Category',y='Review Rating')
fig.show()

7.Are there any notable differences between in purchase behavior between subscribed and non subscribed customers?
# In[98]:


shop.columns


# In[100]:


shop['Subscription Status'].value_counts()


# In[102]:


sns.barplot(shop,x='Subscription Status',y='Purchase Amount (USD)')

8.Which payment method is the most popular among customers?
# In[104]:


shop['Purchase Amount (USD)'].mean()


# In[106]:


shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean()


# In[112]:


shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().sort_values(ascending=False)


# In[114]:


shop_groupby=shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().reset_index()


# In[120]:


fig=px.bar(shop_groupby,x='Payment Method',y='Purchase Amount (USD)')
fig.show()

9.Do customers who use promo codes tend to spend more than those who don't?
# In[122]:


shop_groupby=shop.groupby('Promo Code Used')['Purchase Amount (USD)'].sum().reset_index()


# In[126]:


fig=px.sunburst(shop,path=['Gender','Promo Code Used'], values='Purchase Amount (USD)')
fig.show()


# In[128]:


fig=px.bar(shop_groupby,x='Promo Code Used',y='Purchase Amount (USD)')
fig.show()

10.How does the frequency of purchases vary across different age groups?
# In[130]:


shop[['Age','Age_category']]


# In[132]:


shop['Age_category'].unique()


# In[134]:


shop_group=shop.groupby('Frequency of Purchases')['Age'].sum()


# In[136]:


px.sunburst(shop,path=['Frequency of Purchases','Age_category'],values='Age')

11.Are there any correlations between the size of the product and the purchase amount?
# In[139]:


shop.columns


# In[141]:


shop_group=shop.groupby('Size')['Purchase Amount (USD)'].sum().reset_index()


# In[143]:


fig=px.bar(shop_group,x='Size',y='Purchase Amount (USD)')
fig.show()

12.Which Shipping type is preferred by customers for different product categories?
# In[145]:


shop.groupby('Category')['Shipping Type'].value_counts().sort_values(ascending=False)


# In[147]:


shop['Category'].unique()

13.How does the presence of a discount affect the purchase decision of a customer?
# In[149]:


shop.columns


# In[151]:


shop_group=shop.groupby('Discount Applied')['Purchase Amount (USD)'].sum().reset_index()


# In[153]:


px.histogram(shop_group,x='Discount Applied',y='Purchase Amount (USD)')


# In[155]:


fig=px.sunburst(shop,path=['Gender','Discount Applied'],values='Purchase Amount (USD)', color='Gender')
fig.show()

14.Are there any specific colors that are more popular among customers?
# In[157]:


px.histogram(shop,x='Color')


# In[163]:


shop['Color'].value_counts().nlargest()


# In[165]:


shop['Color'].value_counts()

15.What is the average number of previous purchases made by customers?
# In[167]:


shop['Previous Purchases'].mean()

17.Are there any noticeable differences in purchase behavior between different locations?
# In[169]:


shop.groupby('Location')['Purchase Amount (USD)'].mean().sort_values(ascending=False)


# In[171]:


shop_group=shop.groupby('Location')['Purchase Amount (USD)'].mean().reset_index()


# In[173]:


fig=px.bar(shop_group,x='Location',y='Purchase Amount (USD)')
fig.show()

18.Is there a relationship between customer age and the category of products they purchase?
# In[175]:


shop_group=shop.groupby('Category')['Age'].mean().reset_index()


# In[177]:


fig=px.bar(shop_group,y='Age',x='Category')
fig.show()

19.How does the average purchase amount differ among male and female customers?
# In[179]:


shop_group=shop.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index()


# In[181]:


fig=px.bar(shop_group,x='Gender',y='Purchase Amount (USD)')
fig.show()


# In[183]:


px.sunburst(data_frame=shop,path=['Gender','Age_category'],values='Purchase Amount (USD)')


# In[ ]:




