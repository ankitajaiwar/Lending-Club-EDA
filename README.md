# Lending-Club-EDA
Exploratory data analysis of the famous Lending Club Dataset

Key Insights as observed by doing Exploratory Data Analysis(lca.ipynb) of the Lending Club Dataset:

1. Most of the loan takers are from the state California. But, we can't say anything about people from which state don't repay the loans as almost all the states have the same range of percentage of people(6-14%) who don't repay.

2. Most of the loans are of amount near 10000. People who did not pay back did not have a payment plan. People who fully paid back also didn't have any payment plan. 
   Peope with payment plans are either currently paying or are late by 16-120 days.
   
3. Hardship flag means loan takers due to some harship agreed to pay just interest for a limited period of time. Interestingly the hardship flag is 'NO' for Defauters and Charged- Offs(people from whom there is no expectation of any payment. Its next stage of Defaulter). 

4. There are multiple column pairs with high correlation(>75%). We can surely do well by removing one of the features from such pairs while creating a predictive model.

5. Most loans are lended in B and C grades. Higher the grade, higher the loan amount and hence higher the risk. The risk is confirmed in the above plot as most people who did not pay off took higher grade loans.

6. People in Charged Off and Default category had lower annual incomes than people in other loan status categories.

7. Higher number of credit inquiries results in higher interest rate on loans.
 
8. Most of the loans were taken for deb consolidation, which means most of the loans are taken to pay off other high interest loans.

9. Higher the grade and the risk associated with it, higher the interest rate.

10. People who didn't pay off(loan status : Charged Off and Default), have higher number of credit accounts than people in other loan categories. 


