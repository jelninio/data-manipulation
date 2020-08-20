import pandas as pd

DATA_FILE = "data/Dataset1.xlsx"

# Create a Pandas Dataframe
# (read the Excel data with Pandas)
df = pd.read_excel(DATA_FILE)

#convert column 3 to datetime
df['Experiment date'] = pd.to_datetime(df['Experiment date'])


print(df.iloc[10:40])

#sorting to date/compounds
df_sort = df.sort_values('Compounds',ascending=True)

print(df_sort.iloc[10:40])

#print (df.info())



#df.astype('category').dtypes




#df.info()

#print(df.dtypes[20:30])
#df.to_csv('foo.csv')