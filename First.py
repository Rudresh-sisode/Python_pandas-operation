import pandas as pd
salary=pd.read_csv('Salaries.csv')
mean_year=salary.groupby('Year').mean()['TotalPayBenefits']
print(mean_year)
 #which job title in year 2014 has highest mean salary
mean_title_year=salary.groupby(['Year','JobTitle']).mean()['TotalPayBenefits']
print(mean_title_year)
 #how much money could have been saved in year 2014 by stopping overtimingPay
over_time=salary.groupby('Year').sum()['OvertimePay']
print('we should have saved',over_time)
 #which are the top 5 common job in year 2014 and ...
top_job_title=salary[salary['Year']==2014]['JobTitle'].value_counts().head(5)
print(top_job_title)
 #calculate the cost
sum_cost=0
for index,value in top_job_title.iteritems():
    print(index,value)
    sum_cost+=sum(salary[(salary['Year']==2014) & (salary['JobTitle']==index)]['TotalPayBenefits'])

print('total cost of top 5 jobs in year 2014',sum_cost)
 #who was the top earning employee across all the year
top_sal=salary.groupby('EmployeeName').sum()['TotalPayBenefits']
print((top_sal.sort_values(axis=0)))
