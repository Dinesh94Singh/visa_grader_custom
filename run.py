from datetime import datetime
import json
import csv


fObj = open('./user-data.json',)
data = json.load(fObj)['data']

# print(type(data[0]), data[0])

sorted_values = sorted(data, key=lambda x: (
    datetime.strptime(x['stamping_date'], '%d-%b-%Y')))

# print(sorted_values)

all_content = []

for each in sorted_values:
    content = (each['id'], each['dropoff_city'],
               each['stamping_date'], each['latest_status'], each['mdate'])
    all_content.append(content)

all_content = all_content[::-1]

# print(all_content)

headers = ("ID", "Dropoff City", "Stamping Data",
           "Latest Status", "Last modified date")

with open('./output.csv', 'w') as fw:
    writer = csv.writer(fw)

    writer.writerow(headers)
    writer.writerows(all_content)

chennai_contents = []

for each in all_content:
    if each[1] == "Chennai":
        chennai_contents.append(each)


with open('./output-chennai.csv', 'w') as fw:
    writer = csv.writer(fw)

    writer.writerow(headers)
    writer.writerows(chennai_contents)

print("End of program")
