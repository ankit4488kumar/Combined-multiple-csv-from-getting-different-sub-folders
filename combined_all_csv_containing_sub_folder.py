'''With the help of this you can combined all csv files 
those are containing in a folder but different sub folder of the folder'''

import pandas as pd
import glob
file_path = '/mnt/c/Users/ankit/OneDrive/Documents/abc'


files = glob.glob(file_path+"/*/*.csv")
combined_df = pd.concat([pd.read_csv(f) for f in files])
print(combined_df)
combined_df.to_csv(file_path+"/merged.csv",index=False)
print("All csv has been combined!")
