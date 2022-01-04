# -*- coding: utf-8 -*-

#Pandas Practice

#Import relevant Libraries

import numpy as np
import pandas as pd 

#Importing dataset 

sal = pd.read_csv('Salaries.csv')

#Checking head of dataframe

sal.head()

#checking general information of dataframe

sal.info()

#checking average base pay

avgbasepay = sal['BasePay'].mean()

#checking max overtime pay

maxotpay = sal['OvertimePay'].max()

#JOESPH DRISCOLL job title

jobtitle = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

#Highest paid person

highpay = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']

#average base pay over the years

avgbasepayyears = sal.groupby('Year').mean()['BasePay']

