from fractions import gcd
import sys
import string

LETTER_MAP = string.ascii_letters

#  true if greatest common denominator == 1
def coprime(a, b):
    return gcd(a, b) == 1


def get_key_parts(key):
    keyA = key // len(LETTER_MAP)
    keyB = key % len(LETTER_MAP)
    return keyA, keyB


def check_keys(keyA, keyB, mode):
    if keyA == 1 and mode == 'e':
        sys.exit('keyA=1 too weak.')
    if keyB == 0 and mode == 'e':
        sys.exit('keyB=0 too weak.')
    if keyA < 0 or keyB < 0 or keyB > len(LETTER_MAP) - 1:
        sys.exit('keyA must be greater than 0 and keyB must be between 0 and %s.' % (len(LETTER_MAP) - 1))
    if not coprime(keyA, len(LETTER_MAP)):
        sys.exit('keyA (%s) is not coprime with 52 (a - Z)' % keyA)


def get_cipher_char(plain_char, keyA, keyB):
    plain_char_index = LETTER_MAP.find(plain_char)
    return LETTER_MAP[(plain_char_index * keyA + keyB) % len(LETTER_MAP)]


def get_plain_char(cipher_char, keyA, keyB, mod_inv_a):
    cipher_char_index = LETTER_MAP.find(cipher_char)
    return LETTER_MAP[(cipher_char_index - keyB) * mod_inv_a % len(LETTER_MAP)]
