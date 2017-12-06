
import pandas as pd
import glob
import os


DATA_DIR = './917/'

files = glob.glob(os.path.join(DATA_DIR,'*.csv'))
df_list=[]
for file in files:
    tmp_df = pd.read_csv(file, header=None, encoding="utf-8")
    tmp_df['filename'] = os.path.basename(file)
    df_list.append(tmp_df)
df = pd.concat(df_list, ignore_index=True)

print(df)





