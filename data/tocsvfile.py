import os
import pandas as pd
from glob import glob

# Define the directory containing .dat files
data_folder = '/Users/ismael/Desktop/Data-Balancing/data'

# Get a list of all .dat files in the folder
dat_files = glob(os.path.join(data_folder, '*.dat'))

# Loop through each .dat file in the folder
for file_path in dat_files:
    # Read the file and skip the metadata lines starting with '@'
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Extract column names from the line that contains '@inputs'
    column_names = []
    for line in lines:
        if line.startswith('@inputs'):
            # Strip the '@inputs' part and extract the column names
            column_names = line.replace('@inputs', '').strip().split(', ')
            break

    # Add a column name for the extra target or unknown column if needed
    column_names.append('target')  # Modify 'target' if the last column has a different meaning

    # Read the data part of the .dat file (excluding lines starting with '@')
    data = pd.read_csv(file_path, comment='@', header=None, delim_whitespace=True)

    # Check if the number of columns matches and assign extracted column names to the DataFrame
    if len(column_names) == data.shape[1]:
        data.columns = column_names
    else:
        print(f"Mismatch: {len(column_names)} column names but {data.shape[1]} data columns in file {file_path}.")

    # Save the DataFrame to a CSV file with the same name as the original .dat file
    output_csv = os.path.splitext(file_path)[0] + '.csv'  # Replace .dat with .csv
    data.to_csv(output_csv, index=False)

    print(f"Converted {file_path} to {output_csv}")
