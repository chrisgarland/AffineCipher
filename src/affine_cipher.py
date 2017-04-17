# .../Ass1/AffineCipher/affine_cipher.py
import sys
import os.path
import affine_key as ak
import crypto_math as cm


def main(in_file, mode, init_key):
    if mode is 'e':
        tokens = in_file.name.split('.')
        if tokens[-1] == 'encr':
            sys.exit("ERROR: Attempting to encrypt a file that is already encrypted")
        else:
            encrypt(in_file, init_key)
    elif mode is 'd':
        tokens = in_file.name.split('.')
        if tokens[-1] != 'encr':
            sys.exit("Can only decrypt file with extension: .encr")
        else:
            decrypt(in_file, init_key)


def encrypt(in_file, init_key):
    keyA, keyB = ak.get_key_parts(init_key)
    ak.check_keys(keyA, keyB, 'e')
    file_contents = in_file.readlines()
    f.seek(0)                       # reset file pointer (for overwriting)
    for line in file_contents:
        for c in line:
            if c.isalpha():         # perform shift
                ch = ak.get_cipher_char(c, keyA, keyB)
            else:                   # ignore non-alphabetic characters
                ch = c
            in_file.write(ch)       # overwrite file, one char at a time
    print in_file.name + ' encrypted'
    os.rename(in_file.name, in_file.name + '.encr') # Add file extension


def decrypt(in_file, init_key):
    keyA, keyB = ak.get_key_parts(init_key)
    ak.check_keys(keyA, keyB, 'd')
    mod_inverse_ofA = cm.get_mod_inverse(keyA, len(ak.LETTER_MAP))
    file_contents = in_file.readlines()
    f.seek(0)                       # reset file pointer (for overwriting)
    for line in file_contents:
        for c in line:
            if c.isalpha():         # perform shift
                ch = ak.get_plain_char(c, keyA, keyB, mod_inverse_ofA)
            else:                   # ignore non-alphabetic characters
                ch = c
            in_file.write(ch)       # ovrewrite file, one char at a time
    print in_file.name + ' decrypted'
    os.rename(in_file.name, in_file.name[:-5])  # remove file extension


def numeric(user_input):
    try:
        val = int(user_input)
        return True
    except ValueError:
        return False


def corr_num_args(argv):
    return len(argv) is 4


def corr_order_args(argv):
    return os.path.isfile(argv[1]) and (argv[2] is 'e' or argv[2] is 'd') and numeric(argv[3])


if __name__ == '__main__':
    if corr_num_args(sys.argv) and corr_order_args(sys.argv):
        f = open(sys.argv[1], 'r+')
        main(f, sys.argv[2], int(sys.argv[3]))
        f.close()
    else:
        print 'Invalid args: enter existing filename followed by mode (\'e\' or \'d\'), then the key'
        sys.exit(1)
