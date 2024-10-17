import pandas as pd
 
#creating a variable that is converting a csv file to a dataframe
df = pd.read_csv('./data/timesheet_data.csv')
 
 
#rename columns in my dataframe
df.rename(columns={'Original Entry Date':'Date', 'Quantity Reg':'Hours'}, inplace=True)

# saving the dataframe
df.to_csv('timesheet_export.csv')
 
print(df)


















