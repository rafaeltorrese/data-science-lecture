

def process_date(string):
    if '-' in string:
        average = sum(int(substring) for substring in string.split('-')) / 2
        return round(average)
    return int(string)


if __name__ == '__main__':
    stripped_test_data = ['1912', '1929', '1913-1923',
                          '1951', '1994', '1934',
                          '1915', '1995', '1912',
                          '1988', '2002', '1957-1959',
                          '1955', '1970', '1990-1999']

    processed_test_data = [process_date(year) for year in stripped_test_data]

    print(process_test_data)
