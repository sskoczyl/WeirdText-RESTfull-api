import pytest

from weirdtext_lib.utils import preprocess_encoding, shuffle_word
from weirdtext_lib.excepions import SeparatorAmountException, SeparatorLocalisationException


@pytest.mark.parametrize('to_be_shuffled, expected', [('biiig', 'biiig'), ('Yuuup', 'Yuuup'), ('ooooooO', 'ooooooO')])
def test_shuffle_same_chars(to_be_shuffled, expected):
    assert shuffle_word(to_be_shuffled) == expected


@pytest.mark.parametrize('to_be_shuffled, expected', [('as', 'as'), ('i', 'i')])
def test_shuffle_words_shorter_than_3(to_be_shuffled, expected):
    assert shuffle_word(to_be_shuffled) == expected


@pytest.mark.parametrize('to_be_shuffled, expected', [('', ''), (' ', ' ')])
def test_shuffle_empty_and_space(to_be_shuffled, expected):
    assert shuffle_word(to_be_shuffled) == expected


@pytest.mark.parametrize('to_be_shuffled', [('qwerty'), ('four'), ('equality'), ('shuffle')])
def test_shuffle_empty_and_space(to_be_shuffled):
    assert shuffle_word(to_be_shuffled) != to_be_shuffled


def test_preprocess_encoding(base_coded_sentence, preprocessed_encoded_text, list_of_original_words, separator):
    text, list_of_words = preprocess_encoding(base_coded_sentence, separator)

    assert (text, list_of_words) == (preprocessed_encoded_text, list_of_original_words)


def test_raise_SeparatorsAmountException(wrong_separators_amount, separator):
    for case in wrong_separators_amount:
        with pytest.raises(SeparatorAmountException):
            preprocess_encoding(case, separator)
    

def test_raise_SeparatorLocalisationException(lack_of_first_separator, separator):
    with pytest.raises(SeparatorLocalisationException):
        preprocess_encoding(lack_of_first_separator, separator)

