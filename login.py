import csv
with open('login.csv','w+') as file:
    row=csv.writer(file)
    row.writer(["name","phone number"])
