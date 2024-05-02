import csv

""""""
# Sample data
data = [
    ['Saya Smakova', 87770000000],
    ['Tolqyn Nogaibek', 87470000000],
    ['Sofia Talgat', 87010000001]
]

# Open the CSV file in write mode
with open('sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['first_name','lastname', 'phone_number'])

    # Write the data rows
    for row in data:
        writer.writerow(row)
    