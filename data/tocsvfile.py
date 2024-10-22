import os
import pandas as pd
from glob import glob

data_folder = '/Users/ismael/Desktop/Data-Balancing/data'
dat_files = glob(os.path.join(data_folder, '*.dat'))

for file_path in dat_files:
    with open(file_path, 'r') as f:
        lines = f.readlines()

    column_names = []
    for line in lines:
        if line.startswith('@inputs'):
            column_names = line.replace('@inputs', '').strip().split(', ')
            break

    column_names.append('target')  

    data = pd.read_csv(file_path, comment='@', header=None, delim_whitespace=True)

    if len(column_names) == data.shape[1]:
        data.columns = column_names
    else:
        print(f"Mismatch: {len(column_names)} column names but {data.shape[1]} data columns in file {file_path}.")

    output_csv = os.path.splitext(file_path)[0] + '.csv'  
    data.to_csv(output_csv, index=False)

    print(f"Converted {file_path} to {output_csv}")
