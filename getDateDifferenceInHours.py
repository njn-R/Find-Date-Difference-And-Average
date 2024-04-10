# import pandas as pd

# # Read the first CSV file
# df1 = pd.read_csv('file1.csv')
# # Read the second CSV file
# df2 = pd.read_csv('file2.csv')

# # Merge the two DataFrames on the id column
# merged_df = pd.merge(df1, df2, on='id')

# # Convert the date columns to datetime objects
# merged_df['date_x'] = pd.to_datetime(merged_df['date_x'])
# merged_df['date_y'] = pd.to_datetime(merged_df['date_y'])

# # Calculate the time difference in hours
# merged_df['time_difference_hours'] = (merged_df['date_y'] - merged_df['date_x']).dt.total_seconds() / 3600

# # Output the result to a new CSV file
# merged_df.to_csv('time_difference.csv', index=False)


import csv
from datetime import datetime

# Read the first CSV file into a dictionary
file1_data = {}
with open('file1.csv', 'r') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        file1_data[row['id']] = row['date']

# Read the second CSV file into a dictionary
file2_data = {}
with open('file2.csv', 'r') as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        file2_data[row['id']] = row['date']

# Calculate the time difference in hours for each id
time_differences = {}
for id, date1 in file1_data.items():
    if id in file2_data:
        date2 = file2_data[id]
        datetime1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
        datetime2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
        time_difference_hours = (datetime2 - datetime1).total_seconds() / 3600
        time_differences[id] = time_difference_hours

# Write the time differences to a new CSV file
with open('time_difference.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'time_difference_hours']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for id, difference in time_differences.items():
        writer.writerow({'id': id, 'time_difference_hours': difference})
