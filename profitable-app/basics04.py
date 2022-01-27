# %%
import csv
from pprint import pprint
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

data_path_android = pathlib.Path('profitable-app/data/googleplaystore.csv')
data_path_apple = pathlib.Path('profitable-app/data/AppleStore.csv')
# F: \slides\data-science-lecture\profitable-app\data\AppleStore.csv
# %%

if __name__ == '__main__':
    with open(data_path_android, 'r', encoding='utf-8', newline='') as f:
        header_android = list(next(csv.reader(f)))
        data_android = [*csv.reader(f)]

    with open(data_path_apple, 'r', encoding='utf-8', newline='') as f:
        header_apple = [*next(csv.reader(f))]
        data_apple = [*csv.reader(f)]

    explore_data(data_android, 10470, 10475)

    del data_android[10472]

    # explore_data(data_android, 10470, 10475)
    print(f'Header of Android \n {header_android}')
    app_names = [record[0] for record in data_android]
    unique_app_names = list(set(app_names))
    # print(len(unique_app_names))

    num_duplicates = len(app_names) - len(unique_app_names)
    expected_length = len(app_names) - num_duplicates
    print(
        f'Number of duplicate app names {num_duplicates}')

    # print(unique_app_names[:5])

# %%
    name = unique_app_names[0]
    print(f'App Name: {name}')
    for record in data_android:
        if record[0] == name:
            print(record)

# %%
    print(f'Expected length: {expected_length}')
    # print(len(app_names))

# %%[markdown]
# ## Removing Duplicates
# To remove the duplicates, we will do the following:
#
# - Create a dictionary, where each dictionary key is a unique app name and the corresponding dictionary value is the highest number of reviews of that app.

# - Use the information stored in the dictionary and create a new dataset, which will have only one entry per app (and for each app, we'll only select the entry with the highest number of reviews).

# To turn the steps above into code, we'll need to use the `not in` operator. The `not in` operator is the opposite of the `in` operator. For instance, 'z' in ['a', 'b', 'c'] returns False because 'z' is not in ['a', 'b', 'c'], but 'z' not in ['a', 'b', 'c'] returns True because it's true that 'z' is not in the list ['a', 'b', 'c'].

# %%
    reviews_max = {}
    reviews_index = header_android.index('Reviews')
    for app in data_android:
        name = app[0]
        n_reviews = float(app[reviews_index])
        if reviews_max.get(name, -1) < n_reviews:
            reviews_max.update({
                name: n_reviews
            })

# %%
    print(f'{reviews_max.get("Instagram"):,.0f}')
    print(len(reviews_max))
# %%
    android_clean = []
    already_added = []

    for app in data_android:
        name = app[0]
        n_reviews = float(app[reviews_index])
        if reviews_max.get(name) == n_reviews and name not in already_added:
            android_clean.append(app)
            already_added.append(name)

    print(f'Number of android apps in data cleaned: {len(android_clean)}')
# %%
    pprint(android_clean[:9])
# %%
    id_apple_apps = [app[0] for app in data_apple]
    explore_data(data_apple, 0, 5, True)
    print()
    print(
        f'Number of different id in apple dataset: {len(set(id_apple_apps))}')
# %%
    test_nonenglish_word_list = [
        'Instagram',
        '爱奇艺PPS -《欢乐颂2》电视剧热播',
        'Docs To Go™ Free Office Suite',
        'Instachat 😜',
    ]

    for word in test_nonenglish_word_list:
        print(english_app(word))

# %%
    print(ord('™'))
    print(ord('😜'))
# %%
    for word in test_nonenglish_word_list:
        print(english_app2(word))
# %%
    pprint(header_apple)
# %%
    english_android = [app for app in android_clean if english_app2(app[0])]
    english_apple = [app for app in data_apple if english_app2(app[2])]

    # explore_data(english_android, 0, 3, True)
    # explore_data(english_apple, 0, 3, True)
# %%
    type_index_android = header_android.index('Type')
    price_index_android = header_android.index('Price')
    price_index_apple = header_apple.index('price')

# for i, app in enumerate(english_android):
#     try:
#         float(app[price_index_android])
#     except:
#         print(i, app[price_index_android])

# for i, app in enumerate(english_apple):
#     try:
#         float(app[price_index_apple])
#     except:
#         print(i, app[price_index_apple])
# %%

# %%
    free_android_apps = [
        app for app in english_android if app[type_index_android].lower() == 'free']
    print(len(free_android_apps))

    nonfree_android_apps = [
        app for app in english_android if app[type_index_android].lower() != 'free']
    print(len(nonfree_android_apps))

    for app in english_android:
        price = app[price_index_android]
        if "$" in price:
            price = price.replace('$', '')
        price = float(price)
        app[price_index_android] = price


# %%
    free2 = [app for app in english_android if app[price_index_android] == 0]

    nonfree2 = [
        app for app in english_android if app[price_index_android] != 0]

    print(len(free2))
    print(len(nonfree2))
