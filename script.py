import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob
#collected all the files starting with states, and then gathered them as a csv
files=glob.glob("states*.csv")
list=[]
for file in files:
 list.append(pd.read_csv(file))
us_census=pd.concat(list)
# removed $ sign from Income and split gender population column into men and women population through a string split
us_census['Income']=us_census['Income'].str.split('\$', expand=True)[1]
us_census['Income']=pd.to_numeric(us_census.Income)
print(us_census.head())
us_census['Men']=us_census['GenderPop'].str.split('M', expand=True)[0]
split=us_census['GenderPop'].str.split('_', expand=True)[1]
us_census['Women']=split.str.split('F', expand=True)[0]
us_census.Men = pd.to_numeric(us_census['Men'])
us_census.Women = pd.to_numeric(us_census['Women'])
print(us_census.dtypes)
print(us_census)
us_census['Women']=us_census.Women.fillna(us_census.TotalPop-us_census.Men)
clean_us_census=us_census.drop_duplicates()
print(us_census.duplicated())
plt.subplot(1,1,1)
plt.scatter(x=clean_us_census.Women,y=clean_us_census.Income )
plt.ylabel("Income")
plt.xlabel("Women")
plt.title("Scatter plot between income and women\'s population")
plt.show()

print(clean_us_census.columns)

clean_us_census['Hispanic']=clean_us_census['Hispanic'].str.split("%", expand =True)[0]
clean_us_census['Hispanic']=pd.to_numeric(clean_us_census['Hispanic'])
plt.subplot(2,1,1)
plt.hist(clean_us_census['Hispanic'])
plt.xlabel('Hispanic population')
plt.ylabel('Number of states')
plt.title('Distribution of Hispanic population across states')
plt.show()