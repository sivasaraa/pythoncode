import pandas as pd
import numpy as np

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
print(df)
df['Date'] = ['December 1', 'January 1', 'mid-May']
print("added date column")
print(df)
df['Delivered'] = True
print("added delivered  and feedback column")
df['Feedback'] = ['Positive', None, 'Negative']
print(df)
adf = df.reset_index()
print("added date column")
adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})
print(adf)
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())
print("Outer Join")
print(pd.merge(staff_df,student_df,how='outer',left_index=True,right_index=True))
print("Inner Join")
print(pd.merge(staff_df,student_df,how='inner',left_index=True,right_index=True))
print("Left Join")
print(pd.merge(staff_df,student_df,how='left',left_index=True,right_index=True))
print("Right Join")
print(pd.merge(staff_df,student_df,how='right',left_index=True,right_index=True))
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
print("Inner join by name")
print(pd.merge(staff_df,student_df,how='inner',left_on='Name',right_on='Name'))
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
print("join by first and last name")
print(pd.merge(staff_df,student_df,how='inner',left_on=['First Name','Last Name'],right_on=['First Name','Last Name']))



# idiomatic pandas
df = pd.read_csv('census.csv')
print(df.head())
df.where(df['SUMLEV'] == 50).dropna().set_index(['STNAME','CTYNAME'])\
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min':np.min(data),'max':np.max(data)})

df.head().apply(min_max,axis=1)

rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
print(df.head().apply(lambda x: np.max(x[rows]), axis=1))