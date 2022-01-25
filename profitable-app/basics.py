import csv
import pathlib


data_path_google = pathlib.Path('profitable-app/data/googleplaystore.csv')
data_path_apple = pathlib.Path('profitable-app/data/AppleStore.csv')
# F: \slides\data-science-lecture\profitable-app\data\AppleStore.csv

with open(data_path_google, 'r', encoding='utf-8', newline='') as f:
    data_google = [row for row in csv.reader(f)]

with open(data_path_apple, 'r', encoding='utf-8', newline='') as f:
    data_apple = [row for row in csv.reader(f)]

print(len(data_google))
