import pytest

from weirdtext_lib import weird_text
from weirdtext_lib.excepions import SeparatorAmountException, SeparatorLocalisationException


def test_decoding(base_coded_sentence, base_sentence):
    decoded_text = weird_text.decode(base_coded_sentence)

    assert base_sentence == decoded_text


def test_encoding(base_sentence):
    encoded_text = weird_text.encode(base_sentence)
    decoded_text = weird_text.decode(encoded_text)

    assert base_sentence == decoded_text


@pytest.mark.parametrize('text', [("?///n/'']]|"), ("")])
def test_encoding_decoding_nonliterals(text):
    encoded_text = weird_text.encode(text)
    decoded_text = weird_text.decode(encoded_text)

    assert text == decoded_text


@pytest.mark.parametrize('text', [(""), ("\n-weird-\n"), ("\n-weird-\nasdasd \n-weird-\naddd\n-weird-\n")])
def test_raises_SeparatorAmountException(text):
    with pytest.raises(SeparatorAmountException):
        weird_text.decode(text)


@pytest.mark.parametrize('text', [(" some words\n-weird-\nasdasd \n-weird-\nasdasd")])
def test_raises_SeparatorLocalisationException(text):
    with pytest.raises(SeparatorLocalisationException):
        weird_text.decode(text)
