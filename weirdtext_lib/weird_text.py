import re

from .utils import shuffle_word, preprocess_encoding


def encode(text, *, separator='\n-weird-\n'):
    """
    Function that does WeirdText encoding.

    :param text: string. Text to be encoded.
    :param separator: string, optional. Separator is used to mark start of encoded file an to mark start of original
    words section. Default value is '\n-weird-\n'. Note that separator MUST BE the same during encoding and decoding.
    :return: string. Encoded text.
    """
    tokenize_re = re.compile(r'(\w+)', re.U)
    words_to_encode = [word for word in tokenize_re.findall(text) if
                       (len(word) > 3 and len(set(word[1:-1])) > 1)]  # Remove words of length<=3

    for word in words_to_encode:
        text = text.replace(word, shuffle_word(word))

    text = separator + text + separator + ' '.join(sorted(words_to_encode, key=str.casefold))

    return text


def decode(text, *, separator='\n-weird-\n'):
    """
    Function that does WeirdText decoding.

    :param text: string. Text to be decoded.
    :param separator: string, optional. Separator is used to mark start of encoded file an to mark start of original
    words section. Default value is '\n-weird-\n'. Note that separator MUST BE the same during encoding and decoding.
    :return: string. Decoded text.
    """

    text, original_words = preprocess_encoding(text, separator)

    if len(text) > 0 and text != " ":
        tokenize_re = re.compile(r'(\w+)', re.U)

        decode_keys = [word for word in tokenize_re.findall(text) if
                       (len(word) > 3 and len(set(word[1:-1])) > 1)]  # Remove words of length<=3

        sorted_decode_keys = [word[0] + ''.join(sorted(word[1:-1])) + word[-1] for word in list(decode_keys)]
        sorted_original_words = [word[0] + ''.join(sorted(word[1:-1])) + word[-1] for word in list(original_words)]

        decode_dict = dict(zip(decode_keys, sorted_decode_keys))
        original_dict = dict(zip(sorted_original_words, original_words))

        for key in decode_dict:
            decode_dict[key] = original_dict[decode_dict[key]]
            text = text.replace(key, decode_dict[key])

    return text
