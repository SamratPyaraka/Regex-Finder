# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:25:45 2019

@author: samrat.pyaraka
"""

import re
import csv
import os
import regexs
import pandas as pd


'''
    Load a csv file using csv.reader method.
'''

with open(os.path.join(r"C:\Users\samrat.pyaraka\Desktop\iQreate\public_data", "re1.csv"), 'rU') as file:
    target_doc = csv.reader(file, delimiter=",", quotechar='|')
    ncol=len(next(target_doc)) # Read first line and count columns
    print(ncol)
    
    i = 1 #need to count the rows and also helpful in debugging if the regex fails.
    
    # for loop for iterating through all rows
    for line in target_doc:
        print("-------------start of row------------=", i)
        
        # iterating through all the columns one after another to get each text separately.
        for col in range(0, ncol):
            
            # checking if the text in the row is null
            if line[col] != "":
                
                # creating object of the Class Regex and also passing text of that
                # particular column so that it can be assign and can be used in all
                # functions / methods.
                IsRegexFound = regexs.regexs(line[col], ncol)
                
                # Calling method and getting the regex results
                result = IsRegexFound.checknAssignRegex()
                print(result)
            else:
                print("NULL")
            
        print("-------------end of row------------")
        i += 1
            


#with open(os.path.join(r"C:\Users\samrat.pyaraka\Desktop\iQreate\public_data", "nre2.csv"), 'rU') as file:
#    target_doc = csv.reader(file, delimiter=",", quotechar='|')
#    ncol=len(next(target_doc)) # Read first line and count columns
#    print(ncol)
#    
#    i = 1
#    for line in target_doc:
#        
#        print("-------------start of row------------=", i)
#        for col in range(0, ncol):
#            line[col] = line[col].replace(',', '')
#            line[col] = line[col].strip()
#            if line[col] != "":
#                IsRegexFound = regexs.regexs(line[col], ncol)
#                result = IsRegexFound.CheckNRERegex()
#                print(result)
#            else:
#                print("NULL")
#            
#        print("-------------end of row------------")
#        i += 1
        
        
#dataframe = pd.read_csv(os.path.join(r"C:\Users\samrat.pyaraka\Desktop\iQreate\public_data", "nre2.csv"), error_bad_lines=False, skipinitialspace=True)
#
#i =1
#for index, row in dataframe.iterrows():
#    print("-------------start of row------------=", i)
#    #print(row[0], row[1], row[2])
#    for col in range(0,len(dataframe.columns)):
#        if row[col] != "":
#            IsRegexFound = regexs.regexs(str(row[col]), 0)
#            result = IsRegexFound.CheckNRERegex()
#            
#            print(result)
#        else:
#            print("NULL")
#    print("-------------end of row------------")
#    i += 1
