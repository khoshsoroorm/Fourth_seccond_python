def unique_keywords(text):
    """

    :param text:
    :return: list of unique words
    """
    lst_words = text.split()
    return list(set(lst_words))


print(unique_keywords('hello and lalaal hello hello'))
