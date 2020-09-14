# -*- coding: utf-8 -*-
"""
@author: Nuhammed Ali Kocabey
"""

import pandas as pd

adf = pd.read_csv("olympics.csv", index_col=0, skiprows=1)
df = pd.read_csv("olympics.csv", index_col=0, skiprows=1)


for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df2 = df.copy()

df = df.drop('Totals')


#%%     Question 0 (Example)
            
def answer_zero():
    print("Question 0 - What is the first country in df?")
    
    print("\n", df.iloc[0])
    
    print("\n\n\n")
    
answer_zero()


#%% Question 1 

def answer_one():
    print("Question 1 - Which country has won the most gold medals in summer games?")
    
    print("\n", df['Gold'].idxmax())
    
    print("\n\n\n")
    
answer_one()


#%% Question 2 

def answer_two():
    print("Question 2 - Which country had the biggest difference between their summer and winter gold medal counts?")
    
    print("\n", (df['Gold'] - df['Gold.1']).idxmax())
    
    print("\n\n\n")
    
answer_two()
    

#%% Question 3

def answer_three():
    print("Question 3 - Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?")
    print(" = (Summer Gold - Winter Gold) / Total Gold")
    
    df_more = df[(df['Gold']>=1) & (df['Gold.1']) >=1]
    temp_series = (((df_more['Gold'])-(df_more['Gold.1']))/df_more['Gold.2']).abs()
    answer = (((df_more['Gold'])-(df_more['Gold.1']))/df_more['Gold.2']).abs().argmax()

    print("\n", temp_series.index[3])

    print("\n\n\n")
answer_three()
    

#%% Question 4

def answer_four():
    print("""Question 4 - Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.""")

    df['Points'] = pd.Series((df['Gold.2'] * 3 ) + (df['Silver.2'] * 2) + df['Bronze.2'])
    
    print("\n", df['Points'])
    
    print("\n\n\n")
    
answer_four()





#%%


census_df = pd.read_csv("census.csv", encoding = "ISO-8859-1")


#%% 





#%% Question 5

def answer_five():
    print("Question 5 - Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)")
    
    answer = census_df.groupby(['STNAME']).sum()['COUNTY'].idxmax()
    
    print("\n", answer)
    
    print("\n\n\n")
    
answer_five()


#%% Question 6

def answer_six():
    print("Question 6 - Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.")
    
    answer = census_df[census_df['SUMLEV'] == 50].groupby('STNAME')['CENSUS2010POP'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()

    print("\n", answer)
    
    print("\n\n\n")
    
answer_six()


#%% Question 7

def answer_seven():
    print("Question 7 - Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)")
    
    county_only = census_df[census_df['SUMLEV']==50].set_index('CTYNAME')
    years = ['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
    answer=  (county_only.loc[:, years].max(axis=1) - county_only.loc[:, years].min(axis=1)).argmax()
    
    print("\n", answer)
    
    print("\n\n\n")
    
answer_seven()

