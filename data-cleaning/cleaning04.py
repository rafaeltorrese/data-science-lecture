import csv
from pprint import pprint
# data-cleaning\artworks.csv


def remove_parenthesis(row,  column=2):
    field = row[column]
    field = field.replace('(', '')
    field = field.replace(')', '')
    row[column] = field


if __name__ == '__main__':
    with open('data-cleaning/artworks.csv', encoding='utf-8', newline='') as f:
        header = next(csv.reader(f))
        moma = [*csv.reader(f)]

    num_rows = len(moma)
    print(header)
    print()
    pprint(moma[:3])
    print()
    # index: 2, 3, 4, 5
    for collection in moma:
        for i in [2, 3, 4, 5]:
            remove_parenthesis(collection, column=i)

    gender_index = header.index("Gender")
    print(f'Gender is at index: {gender_index}')

    for collection in moma:
        gender = collection[gender_index]
        gender = gender.title()
        if not gender:
            gender = 'Gender Unknown/Other'
        collection[gender_index] = gender

    nation_index = header.index('Nationality')
    for collection in moma:
        nationality = collection[nation_index]
        nationality = nationality.title()
        if not nationality:
            nationality = 'Nationality Unknown'
        collection[nation_index] = nationality
