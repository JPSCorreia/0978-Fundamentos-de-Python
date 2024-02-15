import csv

# Specify the file path
file_path = './agenda/agenda.csv'

# Data to be written to the CSV file
data_to_write = [
    # ['Name', 'Phone', 'Email'],
    ['John Doe','john.doe@example.com','123-456-7890'],
    ['Jane Smith','jane.smith@example.com','987-654-3210'],
    ['Bob Johnson','bob.johnson@example.com','555-123-4567']
]

# Writing to the CSV file
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write each row
    for row in data_to_write:
        writer.writerow(row)