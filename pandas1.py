import pandas as pd
import numpy as np

#pandas Series
animals = ['Tiger', 'Bear', 'Moose']
a = pd.Series(animals)
print(a)

numbers = [1, 2, 3]
n = pd.Series(numbers)
print(n)

animals = ['Tiger', 'Bear', None]
anw = pd.Series(animals)
print(anw)

print("here none is converted into nan")
numbers = [1, 2, None]
nw = pd.Series(numbers)
print(nw)

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
sp = pd.Series(sports)
print(sp)

print("index",sp.index)
animals = pd.Series(['Tiger','Bear','Elephant'],index=['India','America','Africa'])
print(animals)

print("pandas querying")
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
sp = pd.Series(sports)
print(sp)

print("3 index=",sp.iloc[3])
print("Golf = ",sp.loc['Golf'])

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'],
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)
print("original sports",original_sports)
print("cricket countries",cricket_loving_countries)
print("all countries \n",all_countries)
print("list cricket game from all countries \n",all_countries.loc['Cricket'])


#DataFrame
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
itemdf = pd.DataFrame([purchase_1,purchase_2,purchase_3],index=['store1','store1','store2'])
print("Item dataset \n",itemdf)
print("store2 value = ",itemdf.loc['store2'])
print("type of store2=",type(itemdf.loc['store2']))
print("cost of store1 \n",itemdf.loc['store1','Cost'])
print("transpose \n",itemdf.T)
print("item purchased \n",itemdf.T.loc['Item Purchased'])
print("store1 and cost \n",itemdf.loc['store1','Cost'])
print("Name and cost \n",itemdf.loc[:,('Name','Cost')])
itemdf.drop('store1')
print("after dropping \n",itemdf)
copydf = itemdf.copy()
copydf.drop('store1',inplace=True)
print("copied itemdf \n",copydf)
print("original df \n",itemdf)


#Data frame Indexing and Loading
df = pd.read_csv('olympics.csv',index_col=0,skiprows=1)
print(df.head())
print("list of columns",df.columns)

#changeing the column names
print("changing the column names")
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col:"Gold"+col[5:]},inplace=True)
    if col[:2] == '02':
        df.rename(columns={col:"Silver"+col[5:]},inplace=True)
    if col[:2] == '03':
        df.rename(columns={col:"Bronze"+col[5:]},inplace=True)
    if col[:1] == '№':
        df.rename(columns={col:col[2:]},inplace=True)
print("after column change\n",df.head())

#Querying the Data Frame
only_gold = df[df['Gold']>0]
print("length of gold",len(only_gold))
only_gold = df.where(df['Gold']>0)
print("length of gold",len(only_gold))
print("No of countries have gold",only_gold['Gold'].count())
only_gold.dropna(inplace=True)
print("countries have gold in summer or winter",len(df[(df['Gold']>0) | (df['Gold1']>0)]))
print("countries have only winter gold =",df[(df['Gold'] == 0) & (df['Gold1']>0)].index[0])

#Indexing Dataframe
df['country'] = df.index
df.set_index('Gold',inplace=True)
df.reset_index(inplace=True)
print(df.head())

census = pd.read_csv('census.csv')
print("unique sSUMLEV =", census['SUMLEV'].unique())
census = census[census['SUMLEV'] == 50]
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
census = census[columns_to_keep]
census.set_index(['STNAME','CTYNAME'],inplace=True)
print(census.head())
print(census.loc['Alabama','Autauga County'])
print(census.loc[[('Alabama','Autauga County'),('Alabama','Baldwin County')]])
