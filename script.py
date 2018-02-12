# Import CSV File
# Read the File
# Go through each line
# Select the domain name
# Curl each domain inside http or https
# Write the output in a seperate text file


import csv, requests, os

def get(url):
    cmd = "curl -s -m 10 -o /dev/null -w '%%{http_code}' %s" % url
    print(cmd)
    # look up what os.popen do
    return os.popen("curl -s -o /dev/null -w '%%{http_code}' %s" % url).read()
     

with open('sub-domains.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # next escapes the header
    next(csv_reader)
    
    with open('curl.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        
        for line in csv_reader:
            url = "https://"+line[0]
            resp = get(url)
            csv_writer.writerow([url, resp])
            url = "http://"+line[0]
            resp = get(url)
            csv_writer.writerow([url, resp])