import csv
items =[
    ["apple",50],
    ["banana",35],
    ["orange",20]
]
with open("items.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow({"items","quantity"})
    writer.writerows(items)

    print("CSV file written successfully")