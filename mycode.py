import numpy as np
import pandas as pd
import os

data={'Name':['Alice','Bob','Charlie'],
      'Age':[20,25,30],
      'City':['NewYork','Charlie','Bob']
      }

      

df=pd.DataFrame(data)

# # Adding new row to df for V2
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for V3
new_row_loc2 = {'Name': 'GF2', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)] = new_row_loc2

data="data"
os.makedirs(data,exist_ok=True)

filepath=os.path.join(data,'sample-data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(filepath, index=False)

print(f"CSV file saved to {filepath}")