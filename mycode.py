import pandas as pd
import os

data = {
    'Name' : ['Pavan','Shyam','Ram'],
    'Age':[22,23,21],
    'City':['Vizag','NewYork','Chicago']
}

df = pd.DataFrame(data)


data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")