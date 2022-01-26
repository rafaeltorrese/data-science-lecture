# %%
import csv
import pathlib
# %%


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(f'ID: {start}. NumFields {len(row)}')
        print(row)
        print('\n')
        start += 1

    if rows_and_columns:
        print(f'Number of rows: {len(dataset)}')
        print(f'Number of columns: {len(dataset[0])}')


def english_app(word):
    return all(ord(letter) < 128 for letter in word)


def english_app2(word, threshold=3):
    number_non_english = sum(ord(letter) > 127 for letter in word)
    return number_non_english < threshold


# %%
data_path_google = pathlib.Path('data/googleplaystore.csv')
data_path_apple = pathlib.Path('data/AppleStore.csv')
# F: \slides\data-science-lecture\profitable-app\data\AppleStore.csv
# %%

if __name__ == '__main__':
    with open(data_path_google, 'r', encoding='utf-8', newline='') as f:
        header_google = list(next(csv.reader(f)))
        data_google = [*csv.reader(f)]

    with open(data_path_apple, 'r', encoding='utf-8', newline='') as f:
        header_apple = [*next(csv.reader(f))]
        data_apple = [*csv.reader(f)]

    explore_data(data_google, 10470, 10475)

    del data_google[10472]

    explore_data(data_google, 10470, 10475)
