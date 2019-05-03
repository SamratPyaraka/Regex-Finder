# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:25:45 2019

@author: samrat.pyaraka
"""

import re

class regexs:
    def __init__(self, row, numberOfCols):
        self.row = row 
        self.numberOfCols = numberOfCols
		

    ##################################  NRE Solution Functions #################
    '''
        Common method to check n loop through all other Regex methods.
    '''
    def CheckNRERegex(self):
        
        numericMatchNRE = self.numericNRERegex(self.numberOfCols)
        if numericMatchNRE:
            if numericMatchNRE.group(0) == self.row:
                print("Match Found in Numeric Regex")
                return numericMatchNRE.group(0)
            
        stringMatchNRE = self.stringNRERegex(self.numberOfCols)
        if stringMatchNRE:
            if stringMatchNRE.group(0) == self.row:
                print("Match Found in String Regex")
                return stringMatchNRE.group(0)
            
        dateMatchNRE = self.dateNRERegex(self.numberOfCols)
        if dateMatchNRE:
            if dateMatchNRE.group(0) == self.row:
                print("Match Found in Date Regex")
                return dateMatchNRE.group(0)
            
        alphaNumMatchNRE = self.alphaNumericNRERegex(self.numberOfCols)
        if alphaNumMatchNRE:
            if alphaNumMatchNRE.group(0) == self.row:
                print("Match Found in Alpha Numeric Regex")
                return alphaNumMatchNRE.group(0)
            
        textMatchCol1 = self.textNRERegex(self.numberOfCols)
        if textMatchCol1:
            if textMatchCol1.group(0) == self.row:
                print("Match Found in Text Regex")
                return textMatchCol1.group(0)
        else:
            return ("no match found")
    
    '''
        Method to get the date regex in format of DD-MMM-YY/YYYY
    '''
    def dateNRERegex(self, col):
        match=re.search(r'^\d{2}\-(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\-\d{2,4}$',self.row)
        return match
    
    '''
        Method to get Number regex in format of 1234 | 1234-1224 | 9.09 | 0.09
    '''
    def numericNRERegex(self, col):
        match=re.search(r'^(\d*|\d*\-\d*|0*[1-9]+[0-9]*(?:[.][\d]+)?|0+[.][\d]+)$',self.row)
        return match
    
    '''
        Method to get Word regex in format of abc | ABC | Abc |aBC
    '''
    def stringNRERegex(self, col):
        match=re.search(r'^[a-zA-Z]*$',self.row)
        return match
    
    '''
        Method to get Alpha Numeric regex in format of A123B123| 123AB123 etc.
    '''
    def alphaNumericNRERegex(self, col):
        match=re.search(r'^\w+',self.row)
        return match
    
    
    '''
        Method to get Website URL regex
    '''
    def websiteNRERegex(self, col):
        match = re.search(r'((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+(&[a-zA-Z0-9_]+=\w+)*)?', self.row)
        return match
    
    
    '''
        Method to get if all other regex fails.
    '''
    def textNRERegex(self, col):
        
        match=re.search(r'^[\w+\s\(\)\&\'\-\.\%\,\;\&amp;\/\\\#"]+',self.row)
        return match
                             
    ##########################End Of NRE Solutions Functions####################
    
    
    ##################################  RE Solution Functions #################
    
    def checknAssignRegex(self):
    
        #print(self.row)
        
        siteMatch = self.websiteRegex(self.numberOfCols)
        if siteMatch:
            if siteMatch.group(0) == self.row:
                print("Match Found in Website Regex")
                return siteMatch.group(0)
        
        dateMatch = self.dateRegex(self.numberOfCols)
        if dateMatch:
            if dateMatch.group(0) == self.row:
                print("Match Found in Date Regex")
                return dateMatch.group(0)
        
        numericMatch = self.numericRegex(self.numberOfCols)
        if numericMatch:
            if numericMatch.group(0) == self.row:
                print("Match Found in Numeric Regex")
                return(numericMatch.group(0))
        
        stringMatch = self.stringRegex(self.numberOfCols)
        if stringMatch:
            if stringMatch.group(0) == self.row:
                print("Match Found in String Regex")
                return stringMatch.group(0)
        
        alphaNumericMatch = self.alphaNumericRegex(self.numberOfCols)
        if alphaNumericMatch: 
            if alphaNumericMatch.group(0) == self.row:
                print("Match Found in Alpha Numeric Regex")
                return alphaNumericMatch.group(0)
        else:
            return ("No match found")
    
    
    def dateRegex(self, col):
        match=re.search(r'^\d{2}\-(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\-\d{2,4}$',self.row)
        return match
    
    def numericRegex(self, col):
        match=re.search(r'^(\d*|\d*\-\d*)$',self.row)
        return match
    
    def stringRegex(self, col):
        match=re.search(r'^[a-zA-Z]*$',self.row)
        return match
    
    def alphaNumericRegex(self, col):
        match=re.search(r'^\w+',self.row)
        return match
    
    def websiteRegex(self, col):
        match = re.search(r'((ftp|http|https):\/\/)?(www.)?(?!.*(ftp|http|https|www.))[a-zA-Z0-9_-]+(\.[a-zA-Z]+)+((\/)[\w#]+)*(\/\w+\?[a-zA-Z0-9_]+=\w+(&[a-zA-Z0-9_]+=\w+)*)?', self.row)
        return match
                             
    ##########################End Of RE Solutions Functions####################
	