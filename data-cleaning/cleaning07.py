import csv
from pprint import pprint
# data-cleaning\artworks.csv


def remove_parenthesis(row,  column=2):
    field = row[column]
    field = field.replace('(', '')
    field = field.replace(')', '')
    row[column] = field


def convert_date(date):
    if date:
        return int(date)


def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, '')
    return string


def process_date(string):
    if '-' in string:
        average = sum(int(substring) for substring in string.split('-')) / 2
        return round(average)
    return int(string)


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

    for collection in moma[:5]:
        birth_date = collection[3]
        death_date = collection[4]
        print([birth_date, death_date])

    for collection in moma:
        birth = convert_date(collection[3])
        death = convert_date(collection[4])
        collection[3], collection[4] = birth, death

    for collection in moma:
        date = strip_characters(collection[6])
        date = process_date(date)
        collection[6] = date
