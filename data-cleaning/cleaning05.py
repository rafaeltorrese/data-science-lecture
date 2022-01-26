

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, '')
    return string


if __name__ == '__main__':
    test_data = ["1912", "1929", "1913-1923",
                 "(1951)", "1994", "1934",
                 "c. 1915", "1995", "c. 1912",
                 "(1988)", "2002", "1957-1959",
                 "c. 1955.", "c. 1970's",
                 "C. 1990-1999"]

    bad_chars = ["(", ")", "c", "C", ".", "s", "'", " "]

    stripped_test_data = [strip_characters(string) for string in test_data]
    print(stripped_test_data)
