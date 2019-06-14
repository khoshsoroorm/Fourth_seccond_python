# def unique_keywords(text, ):
#     """
#
#     :param text:
#     :return: list of unique words
#     """
#     lst_words = text.split()
#     return list(set(lst_words))


def unique_keywords(text:str, ignore_case=False):
    """

    :param text:
    :return: list of unique words with lower case
    """
    if ignore_case:
        text = text.lower()
    lst_words = text.split()
    return list(set(lst_words))


text = 'Hello AnD aNd lalaal hello hello'
print(unique_keywords(text, True))
