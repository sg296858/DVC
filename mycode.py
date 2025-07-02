import numpy as np
import pandas as pd
import os

data={'Name':['Alice','Bob','Charlie'],
      'Age':[20,25,30],
      'City':['NewYork','Charlie','Bob']
      }

df=pd.DataFrame(data)

data="data"
os.makedirs(data,exist_ok=True)

filepath=os.path.join(data,'sample-data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(filepath, index=False)

print(f"CSV file saved to {filepath}")