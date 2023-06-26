# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 13:41:38 2023

@author: aman_rawat
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Method to read json file and store its data into a 
variable.
"""
json_file = open('loan_data_json.json')
data = json.load(json_file)

"""
Method of turning list data into a dataframe using
pandas.
"""
loan_data = pd.DataFrame(data)

"""
Suppose we want the unique records of a specific column 
then we can use unique function.
"""
loan_data['purpose'].unique()

"""
Basically describing the loan data. We can do it either on 
the whole data or a specific column.
"""
loan_data.describe()

loan_data['credit.policy'].describe()
loan_data['fico'].describe()

"""We used exp function that is used to compute the exponent 
of all values present in the given records.
"""
income = np.exp(loan_data['log.annual.inc'])

"""
Then we store the income in the loan data.
"""
loan_data['annualincome'] = income

"""
This is the fico range that we have to set up in the data.
fico >= 300 and < 400:
'Very Poor'
fico >= 400 and ficoscore < 600:
'Poor'
fico >= 600 and ficoscore < 660:
'Fair'
fico >= 660 and ficoscore < 700:
'Good'
fico >=700:
'Excellent'
"""
length = len(loan_data)  
fico_desc = []
for i in range(0,length):
    """
    Iterates one by one and states category whether it is 
    poor, good or excellent.
    """
    desc = loan_data['fico'][i]
    
    try:
        if desc >= 300 and desc < 400:
            sets = 'Very Poor'
        elif desc >= 400 and desc < 600:
            sets = 'Poor'
        elif desc >= 600 and desc < 660:
            sets = 'Fair'
        elif desc >=660 and desc < 700:
            sets = 'Good'
        elif desc >= 700:
            sets = 'Excellent'
        else:
            sets = 'Unknown Value'
    except:
        sets = 'Unkknown Value'
    fico_desc.append(sets)
    
"""
Converting dataframe object to series beacuse to store it 
in the real data.
"""
fico_desc = pd.Series(fico_desc)

loan_data['fico_category'] = fico_desc

"""
Creating a new column if interest rate is greater than 
mark it as high otherwise low.
"""
loan_data.loc[loan_data['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loan_data.loc[loan_data['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

"""
Grouping specific column to get the number of records in it.
"""
category_plot = loan_data.groupby(['fico_category']).size()
"""
Making plots using the matplotlib.
"""
category_plot.plot.bar(color = 'green')
plt.show()

purpose_wise = loan_data.groupby(['purpose']).size()
purpose_wise.plot.bar(color='red')
plt.show()

"""
scatter plot
"""
xpoint = loan_data['dti']
ypoint = loan_data['annualincome']
plt.scatter(xpoint, ypoint)
plt.show()

"""
writing to csv.
"""
loan_data.to_csv('bank_cleaned.csv', index = True)
