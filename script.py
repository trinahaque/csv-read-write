# Import CSV File
# Read the File
# Go through each line
# Select the domain name
# Curl each domain inside http or https
# Write the output in a seperate text file


import csv

with open('sub-domains.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    
    with open('curl.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        
        for line in csv_reader:
            csv_writer.writerow([line[0]])