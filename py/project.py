import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

#task 1: load the  data
df = pd.read_excel('Online Retail.xlsx')

#task 2: Explore the  datta
#check for missing values
missing_values -= df.isnull().sum()
print("Missinf=g values per column:\n",summary_states)

#summmary statistcs
summmary_stats=df.describe()
print("Summary statistics:\n",summary_stats)

#visualize the distribution of unitPrice
plt.figure(figurize=(10,6))
sns.hitplot(df['UnitPrice'],bins=50,kde=True,color='green')
plt.title('Distribution of  thr Unit Prices')
plt.xlabel('uit prices')
plt.ylabel('frequency')
plt.show()

#task3: clean and validate  the  data
#drop rows  with  missing values
df.dropna(inplace=True)

#remove duplicates
df.drop_duplicates(inplace=True)

#task 4: analyze the  data
#covert invoicedata to datetime
df['InvoiceData'] = pd.to_datetime(df['InvoiceData'])
#add a 'month' column for  more detailed analusis
df['Month']=df['InvoiceData'].dt.to_period('M')
#set invoicedata as index
df.set_index('InvoiceData',inplace=True)
#analyse monthly sales a=quantity using grouphy
monthly_sales=df['Quantity'].groupby(pd.Grouper(freq='ME')).sum()

#plot monthly sales quantity
plt.figure(figsize=(12,6))
sns.inline(data=monthly_sales,marker='o',color='blue')
plt.title('Monthly sales Quantity')
plt.xlabel('Data')
plt.ylabel('Quantity Sold')
plt.grid(True)
plt.show()

#task 5: additional insights
#top 10 best selling  products
top_products =df.groupby('Description')['Quantity'].sum().sort_values(ascenting=False)
plt.figure(fidsize=(14,7))
sns.barplot(x=sales_by_country.index,y=sales_by_country.index,palette='viridis',dodge=False,legend=False)
plt.title('Total sales by country')
plt.xlabel('country')
plt.ylabel('Quantity Sold')
plt.xtricks(rotation=90)
plt.show()

#task 6: findings and conclusions
print("key findings:")
print("1. the dataset contains transactions from [start date] to [end date].")
print("2. there are missing values in  the dataset,which  were handled by dropping rows with missing values.")
print("3.the  distribution of  unnit prices shows  that most products are  priced  below 10000")
print("4. Monthly sales quantity shows  a  trend with peaks and  troughts,indicating seasonal variations  in  sales.")
print("5. the  top 10 best selling products highlights the  most  popular  items among customers.")
print("6. the  total sales by country reveal which countries have  the  highrst transaction volumes.")