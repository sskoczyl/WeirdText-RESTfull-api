import pytest

from weirdtext_lib import weird_text


def test_decoding(base_coded_sentence, base_sentence):
    decoded_text = weird_text.decode(base_coded_sentence)

    assert base_sentence == decoded_text


def test_encoding(base_sentence):
    encoded_text = weird_text.encode(base_sentence)
    decoded_text = weird_text.decode(encoded_text)

    assert base_sentence == decoded_text


def test_encoding_decoding_empty():
    encoded_text = weird_text.encode("")
    decoded_text = weird_text.decode(encoded_text)

    assert "" == decoded_text
