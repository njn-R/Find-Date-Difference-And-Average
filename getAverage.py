import csv

# Define the file path
file_path = 'time_difference.csv'

# Initialize variables to calculate sum and count
total_time_difference = 0
count = 0

# Read the CSV file and calculate the sum of time differences
with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        total_time_difference += float(row['time_difference_hours'])
        count += 1

# Calculate the average
average_time_difference = total_time_difference / count

print("Average time difference:", average_time_difference)
