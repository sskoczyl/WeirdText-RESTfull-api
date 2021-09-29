import random
import re

from .excepions import SeparatorAmountException, SeparatorLocalisationException


def shuffle_word(word):
    """
    Helper function thar does the world shuffling. Randomly mixes order of characters in given world,
    except of first and last character. E.g. 'shuffling' can become 'sflnhfiug'. Function SHOULD NOT be used outside of
    this module. If every character, except first and the last, is the same function returns not shuffled word.

    :param word: string. Word to be shuffled.
    :return: string. Shuffled word.
    """
    was_shuffled = False

    while not was_shuffled:
        if len(set(word[1:-1])) > 1:  # Check if chars (except first and last) in string are not the same
            shuffle_list = list(word[1:-1])
            random.shuffle(shuffle_list)
            shuffled_word = word[0] + ''.join(shuffle_list) + word[-1]

            was_shuffled = True if shuffled_word != word else False

        else:
            shuffled_word = word
            was_shuffled = True

    return shuffled_word


def preprocess_encoding(text, separator):
    """
    Function that splits encoded message using separator value. Returns tuple of string and list- encoded text and
    list of original words. Function raises SeparatorAmountException in case if there is wrong amount of separators,
    and SeparatorLocalisationException if there is no separator at the beginning of the text.

    :param text: string. Encoded text
    :param separator: string.
    :return: tuple. First value of the tuple is encoded text, second value is list with original words
    """
    separator_count = sum(1 for _ in re.finditer(separator, text))

    if separator_count != 2:  # If amount of separators is not equal 2
        raise SeparatorAmountException(
            "Encoded text should have two separators!"
        )

    if not text.lstrip(' ').startswith(separator):  # If there are others characters than separator at the beginning
        raise SeparatorLocalisationException(
            "No separator at the beginning of the encoded text!"
        )

    _, text_separated, words_separated = text.split(separator)

    return text_separated, words_separated.split(' ')
