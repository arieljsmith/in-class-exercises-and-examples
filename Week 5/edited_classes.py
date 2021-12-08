# Warm Up - fix this function.

# This function is supposed to take a list of words and return a new
# list with the one-letter words removed. It's not doing that. First,
# run the function with some test word lists to see what it is doing
# then fix it so it has the desired output.

def remove_single_letter_words_only(word_list):
    new_word_list = []
    for word in word_list:
        if (len(str(word)) > 1) or (len(str(word)) < 1) or isinstance(word, int) or isinstance(word, float):
            new_word_list.append(word)
    return new_word_list


def keep_only_multiletter_words(word_list):
    new_word_list = []
    for word in word_list:
        if isinstance(word, str) and (len(str(word)) > 1):
            new_word_list.append(word)
    return new_word_list


# ======================


word_list = ["hi", "a", "z", "xylophone", "b", "", "us", "rat", 4, 42, 4.20]
print(f"Initial word list is: {word_list}")

new_word_list_1 = remove_single_letter_words_only(word_list)
print(f"New word list with ONLY single-letter words removed: {new_word_list_1}")

new_word_list_2 = keep_only_multiletter_words(word_list)
print(f"New word list that keeps ONLY multi-letter words: {new_word_list_2}")
