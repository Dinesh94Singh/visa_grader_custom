from datetime import datetime
import json
import csv
import requests

url = "https://visagrader.com/api/trackers/dropbox/list"
payload = 'draw=1&start=0&length=300&search%5Bregex%5D=false&search%5Bvalue%5D='

cookie = None
with open('cookie.txt', 'r') as fr:
    cookie = fr.read()

if cookie:
    print("using cookie")

headers = {
    'Cookie': cookie,
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

obj = json.loads(response.text)
data = obj['data']

json_object = json.dumps(data, indent=4)

with open('user-data.json', 'w') as fw:
    fw.write(json_object)

print("total records = ", obj['recordsTotal'])
# fObj = open('./user-data.json',)
# data = json.load(fObj)['data']

# print(type(data[0]), data[0])

sorted_values = sorted(data, key=lambda x: (
    datetime.strptime(x['stamping_date'], '%d-%b-%Y')))

# print(sorted_values)

all_content = []

for each in sorted_values:
    content = (each['id'], each['dropoff_city'],
               each['stamping_date'], each['visa_type'], each['latest_status'], each['mdate'])
    all_content.append(content)

all_content = all_content[::-1]

# print(all_content)

headers = ("ID", "Dropoff City", "Stamping Data", "Visa Type",
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
