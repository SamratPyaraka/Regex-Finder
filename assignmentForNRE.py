# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:09:40 2019

@author: samrat.pyaraka
"""


import re
import csv
import os
import regexs
import pandas as pd
import numpy as np

       
'''
    I am working on window, Please replace the path file as of your requirement.
    This file loads the CSV file from the public_data folder. As all NRE files
    are not cleaned CSV files ex:- few texts have ""(quotes) and (,) commas
    where as other donts. Thats why I have to use dataframes to load and clean
    CSV files.
'''
dataframe = pd.read_csv(os.path.join(r"C:\Users\samrat.pyaraka\Desktop\iQreate\public_data", "nre6.csv"), error_bad_lines=False, skipinitialspace=True)
dataframe = dataframe.replace(np.nan, '', regex=True)
#dataframe.where(dataframe.notnull(), None)
i =1 #need to count the rows and also helpful in debugging if the regex fails.

# for loop for iterating through all rows
for index, row in dataframe.iterrows():
    print("-------------start of row------------=", i)
    
    # iterating through all the columns one after another to get each text separately.
    for col in range(0,len(dataframe.columns)):
        
        # checking if the text in the row is null
        if row[col] != "":
            
            # creating object of the Class Regex and also passing text of that
            # particular column so that it can be assign and can be used in all
            # functions / methods.
            IsRegexFound = regexs.regexs(str(row[col]), 0)
            
            # Calling method and getting the regex results
            result = IsRegexFound.CheckNRERegex()
            
            
            print(result)
        else:
            print("NULL")
    print("-------------end of row------------")
    i += 1
