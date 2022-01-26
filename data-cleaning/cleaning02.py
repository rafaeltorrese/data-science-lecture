import csv
# data-cleaning\artworks.csv
with open('data-cleaning/artworks.csv', encoding='utf-8', newline='') as f:
    next(csv.reader(f))
    moma = [*csv.reader(f)]

print(moma[:2])
num_rows = len(moma)
print(num_rows)
