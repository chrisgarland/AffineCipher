# .../Ass1/AffineCipher/affine_cipher.py
import sys
import os.path

shift = 27


def main(in_file, mode):
    if mode is 'e':
        encrypt(in_file)
    elif mode is 'd':
        tokens = in_file.name.split('.')
        if tokens[2] != 'encr':
            print "Can only decrypt file with extension: '.encr'"
            sys.exit(1)
        else:
            decrypt(in_file)


def encrypt(in_file):
    file_contents = in_file.readlines()
    f.seek(0)
    for line in file_contents:
        for c in line:
            if c.isalpha():
                ch = chr(ord(c)+(shift % 26))
            else:
                ch = c
            in_file.write(ch)
    print in_file.name + ' encrypted'
    os.rename(in_file.name, in_file.name + '.encr')


def decrypt(in_file):
    file_contents = in_file.readlines()
    f.seek(0)
    for line in file_contents:
        for c in line:
            if c.isalpha():
                ch = chr(ord(c)-(shift % 26))
            else:
                ch = c
            in_file.write(ch)


def corr_num_args(argv):
    return len(argv) is 3


def corr_order_args(argv):
    return os.path.isfile(argv[1]) and (argv[2] is 'e' or argv[2] is 'd')


if __name__ == '__main__':
    if corr_num_args(sys.argv) and corr_order_args(sys.argv):
        f = open(sys.argv[1], 'r+')
        main(f, sys.argv[2])
        f.close()
    else:
        print 'Invalid args: enter existing filename followed by \'e\' or \'d\''
        sys.exit(1)
