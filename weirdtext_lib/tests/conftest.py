import pytest


@pytest.fixture()
def base_sentence():
    return "This ia a long looong test sentence, \nwith some big (biiiig) words!"


@pytest.fixture()
def base_coded_sentence():
    return "\n-weird-\nTihs ia a lnog loonog tset stnceene, \nwtih smoe big (biiiig) wrdos!\n-weird-\n" \
           "long looong sentence some test This with words"


@pytest.fixture()
def preprocessed_encoded_text():
    return "Tihs ia a lnog loonog tset stnceene, \nwtih smoe big (biiiig) wrdos!"


@pytest.fixture()
def list_of_original_words():
    return ['long', 'looong', 'sentence', 'some', 'test', 'This', 'with', 'words']


@pytest.fixture()
def separator():
    return "\n-weird-\n"


@pytest.fixture()
def wrong_separators_amount():
    return [" \n-weird-\n some words who cares", " \n-weird-\n some words\n-weird-\n who cares\n-weird-\n"]


@pytest.fixture()
def lack_of_first_separator():
    return " Tihs ia \n-weird-\n a lnog loonog tset stnceene, \nwtih smoe big (biiiig) wrdos!\n-weird-\nThis" \
           " long looong sentence some test This with words"
