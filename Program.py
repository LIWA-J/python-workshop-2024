import pandas as pd
 
#Creating a variable that is converting a csv file to a dataframe
df = pd.read_csv('./data/timesheet_data.csv')
 
#Rename columns in my dataframe
df.rename(columns={'Original Entry Date':'Date', 'Quantity Reg':'Hours'}, inplace=True)
 
#Filter columns
filtered_df = df[['Date', 'Employee Name', 'Hours']]
 
# saving the dataframe
filtered_df.to_csv('timesheet_export.csv')
 
print(filtered_df)

















