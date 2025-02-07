import pandas as pd
import os

data = {
    'Name' : ['Pavan','Shyam','Ram'],
    'Age':[22,23,21],
    'City':['Vizag','NewYork','Chicago']
}

df = pd.DataFrame(data)

new_row_loc = {
    'Name':'GF1',
    'Age':20,
    'City':'Hyd'
}
df.loc[len(df.index)] = new_row_loc

new_row_loc2 = {
    'Name':'GF2',
    'Age':30,
    'City':'Hyd'
}
df.loc[len(df.index)] = new_row_loc2



data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")