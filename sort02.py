import pandas as pd

DATA_FILE1 = "data/Dataset1.xlsx"
DATA_FILE2 = "data/Dataset2.xlsx"

# Create a Pandas Dataframe
# (read the Excel data with Pandas)
df1 = pd.read_excel(DATA_FILE1)
df2 = pd.read_excel(DATA_FILE2)

#concatenate two DataFrame
df = pd.concat([df1,df2])

#convert column 3 to datetime


df['Experiment date'] = pd.to_datetime(df['Experiment date'])

#sorting to date/Compounds
#df = df.sort_values('Compounds', ascending=True)



#Delete all but 5 latest values.
date_today = pd.to_datetime('today').date()

df_range = pd.date_range(end=date_today, freq='W', periods=4)

df_range = df_range[0].date()

#change index to date
df = df.set_index(['Experiment date'])
#sorting index
df = df.sort_values('Experiment date', ascending=True)




print(df.loc[df_range : date_today])




#print (df.tail(20))

#DAta output
#df.to_csv('foo.csv')